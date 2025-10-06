### Calculation model ###


from dataclasses import dataclass, field
import datetime
from decimal import Decimal, InvalidOperation
import logging
from typing import Any, Dict

from app.exceptions import OperationError


@dataclass
class Calculation:
    """
    value object representing a single calcualtion

    This class encapsulates the details of a mathematical calculation, including the
    operation performed, operands invalovled, the result and the timestamp
    of the calculation. It provides methods for performing calculation,
    serializing the data for storage, and deserializing the data to recreate a calcualtion instantce

    # required fields
    operation: str
    operand1: Decimal
    operand2: Decimal

    #fields with default values
    """
    operation: str
    operand1: Decimal
    operand2: Decimal
    result: Decimal = field(init=False) # result of the calculation
    timestamp: datetime.datetime = field(default_factory=datetime.datetime.now) # time when calculation performed

    def __post_init__(self):
        """Post initialization processing
        Automatically calculates result of operation after Calculation instance
        is created
        """
        self.result = self.calculate()
    
    def calculate(self) -> Decimal:
        """
        Execute calculation using specified operation
        Utilizes a dictionary to map operation names to their corresponding lambda functions,
        enabling dynamic execution of operations based on the operation name
        
        Returns: 
            Decomal, the result of the calculation

        Raises:
            OperationError if the operation is unknwon or the calculation fails.
        
        """
        # Mapping operation names to corrresponding function
        operations = {
            "Addition": lambda x, y: x + y,
            "Subtraction": lambda x, y: x - y,
            "Multiplication": lambda x, y: x* y,
            "Division": lambda x, y: x / y if y != 0 else self._raise_div_zero(),
            "Power": lambda x, y: Decimal(pow(float(x), float(y))) if y >= 0 else self._raise_neg_power(),
            "Root": lambda x, y: (
                Decimal(pow(float(x), 1 / float(y)))
                if x >= 0 and y !=0
                else self._raise_invalid_root(x, y)
            )
        }

        # retrieves the operation based on operation name

        op = operations.get(self.operation)
        if not op: 
            raise OperationError(f"Unknown operation: {self.operation}")
        try:
            #Execute the opeartion with provided operands
            return op(self.operand1, self.operand2)
        except (InvalidOperation, ValueError, ArithmeticError) as e:
            # Handle any errors that occur in calculation
            raise OperationError(f"Calculation failed: {str(e)}")
        

    @staticmethod
    def _raise_div_zero(): # pragma: no cover
        """
        Helper method to raise vision by zero error
        This method is called when division by zero is attempted
        """
        raise OperationError("Division by zero is not allowed")
    
    @staticmethod
    def _raise_neg_power(): # pragma: no cover
        """
        Helper method to raise negative power error
        This method is called when a negative exponent is used in power operation
        """
        raise OperationError("Negative exponents are not supported")
    @staticmethod
    def _raise_invalid_root(x: Decimal, y: Decimal): # pragma: no cover
        """
        Helper method for invalid root error

        ARGS:
            x, Decimal: number from which the root is taken
            y, Decimal, the degree of the root
        """    
        if y == 0:
            raise OperationError("Zero root is undefined")
        if x < 0:
            raise OperationError("Cannot calculate root of negative number")
        raise OperationError("Invalid root operation")
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert calculation to dictionary for serialization
        THis method transforms the calculation instance into a dictionary format
        facilitating easy storage and retrieval e.g. saving to a file
        Returns:
            Dict[str, Any]: a dictionary containing the calculation data in a serializable format

        """
        return {
            'operation': self.operation,
            'operand1': str(self.operand1),
            'operand2': str(self.operand2),
            'result': str(self.result),
            'timestamp': self.timestamp.isoformat()
        }
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Calculation':
        """
        Create calculion from dictionary

        This method reconstructs a Calculation instance from a dictionary ensuring
        all required fields are present and correctly formatted

        ARGS:
            data (Dict[str, Any]) : Dictionary containing calculation data
        Returns: 
            Calculation: a new instance of Calculation with data populated from the dictionary

        Raises:
            OperationError: if data is invalid or missing required fields
        """
        try: 
            calc = Calculation(
                operation=data['operation'],
                operand1=Decimal(data['operand1']),
                operand2=Decimal(data['operand2'])
            )
            # set timestamp
            calc.timestamp = datetime.datetime.fromisoformat(data['timestamp'])

            saved_result = Decimal(data['result'])
            if calc.result != saved_result:
                logging.warning(
                    f"Loaded calculation result {saved_result}"
                    f"differs from computed result {calc.result}"
                ) # pragma: no cover
            return calc
        except (KeyError) as e:
            raise OperationError(f"Invalid calculation data: {str(e)}")

    def __str__(self) -> str:
        """
        Return string representation of calculation
        Provides human readable representation of the calculation, with the operation
        performed and its result

        Returns:
            str: Formatted string showing the calculation and result
        """
        return f"{self.operation}({self.operand1}, {self.operand2}) = {self.result}"
    
    def __repr__(self) -> str:
        """
        String DETAILED representation
        useful for debugging, unambiguous string operation
        """
        return (
            f"Calculation(operation='{self.operation}',"
            f"operatnd1={self.operand1}, "
            f"operand2={self.operand2}, "
            f"result-{self.result}, "
            f"timestamp='{self.timestamp.isoformat()}')"
        )
    
    def __eq__(self, other: object) -> bool:
        """
        Check if two calculations are equal.

        Compares two Calculation instances to determine if they represent the same
        operation with identical operands and results.

        Args:
            other (object): Another calculation to compare with.

        Returns:
            bool: True if calculations are equal, False otherwise.
        """
        if not isinstance(other, Calculation):
            return NotImplemented
        return (
            self.operation == other.operation and
            self.operand1 == other.operand1 and
            self.operand2 == other.operand2 and
            self.result == other.result
        )

    def format_result(self, precision: int = 10) -> str:
        """
        Format the calculation result with specified precision.

        This method formats the result to a fixed number of decimal places,
        removing any trailing zeros for a cleaner presentation.

        Args:
            precision (int, optional): Number of decimal places to show. Defaults to 10.

        Returns:
            str: Formatted string representation of the result.
        """
        try:
            # Remove trailing zeros and format to specified precision
            return str(self.result.normalize().quantize(
                Decimal('0.' + '0' * precision)
            ).normalize())
        except InvalidOperation:  # pragma: no cover
            return str(self.result)
