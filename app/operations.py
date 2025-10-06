### OPERATION CLASSES ###

from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict

from app.exceptions import ValidationError

class Operation(ABC):
    """
    Abstract base clase for calculators operations
    Defines the interface for all operations.
    Each operation MUST IMPLEMENT the execute method and can optionally override operand validation

    Whenever you add a new operation you add a new class
    it can implement validate operands and execute however it wants and theres no need to update the main code
    """

    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal: 
        """
        Execute the operation

        Performs the arithmetic operation on the inserted operands
        ARGS:
            a (Decimal): First operand.
            b (Decimal): Second operand.
        REturns:
            DEcimal: result of the operation
        Raises: 
            OperationError: If the operation Fails
        """
        pass # pragma: no cover
    def validate_operands(self, a: Decimal, b: Decimal) -> None:
        """
        Validate operands before execution.
        Can be overriden by subclasses to enforce specific validation rules for different operations.
        Args:
            a (Decomal): first operand.
            b (Decomal): second operand.
        Raises:
            ValidationError: If operands are invalid.
        """
        pass

    def __str__(self) -> str:
        """
        Return operation name for display
        Provides a string representation of the operation, typically the class name
        Returns:
            str: name of the operation
        """
        return self.__class__.__name__
    
# Operantions class uses another class for each operation

class Addition(Operation):
    """
    Addition operation implementation
    Performs the addition of two numbers
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        self.validate_operands(a, b)
        return a + b
    
class Subtraction(Operation):
    """
    Subtraction operation implementation
    Performs the subtraction of two numbers
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Subtract one number from another 
        ARGS:
            a (Decimal): First operand
            b (Decimal): Second operand
        Returns: 
            Decomal: Difference between two operands
        """
        self.validate_operands(a, b) 
        return a - b
    

class Multiplication(Operation):
    """
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Multiply two numbers
        a: Decimal, first operand
        b: Decimal, second operand
        """
        self.validate_operands(a,b)
        return a * b

class Division(Operation):
    """
    Division operation implementation
    Performs division of one number by another

    """
    def validate_operands(self, a: Decimal, b: Decimal) -> None:
        """
        Validate operands checking for division by zero
        Args:
            a: Decimal, Dividend
            a: Decimal, Divisor
        Raises:
            ValidationError if the divisor is zero.
        """
        super().validate_operands(a, b)
        if b == 0:
            raise ValidationError("Division by zero is not allowed")
    
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Divide one number by another
        ARGS:
            a: Decimal, Divident
            b: Decimal, Divisor
        Returns:
            Decimal, quotient of the division
        """
        self.validate_operands(a, b) #implemented above for the division situation
        return a / b

class Power(Operation):
    """
    Power (exponentiation) operation implementation
    Raises one number to the power of another 
    """

    def validate_operands(self, a: Decimal, b:Decimal) -> None:
        super().validate_operands(a, b)
        if b < 0:
            raise ValidationError("Negative exponents not supported")
        
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Calculate one number raised to the power of another
        ARGS:
            a, Decimal: base number
            b, Decimal: exponent
        Returns:
            Decimal, result of the exponentiation
        """
        self.validate_operands(a, b)
        return Decimal(pow(float(a), float(b)))
    
class Root(Operation):
    """
    Root operation implementation
    Calculates the nth root of a number
    """
    def validate_operands(self, a: Decimal, b: Decimal) -> None:
        """
        Validate operands for root operation.

        Overrides the base class method to ensure that the number is non-negative
        and the root degree is not zero.

        Args:
            a (Decimal): Number from which the root is taken.
            b (Decimal): Degree of the root.

        Raises:
            ValidationError: If the number is negative or the root degree is zero.
        """
        super().validate_operands(a, b)
        if a < 0:
            raise ValidationError("Cannot calculate root of negative number")
        if b == 0:
            raise ValidationError("Zero root is undefined")

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """
        Calculate the nth root of a number.

        Args:
            a (Decimal): Number from which the root is taken.
            b (Decimal): Degree of the root.

        Returns:
            Decimal: Result of the root calculation.
        """
        self.validate_operands(a, b)
        return Decimal(pow(float(a), 1 / float(b)))

class OperationFactory:
    """
    Factory class for creating operation instances
    Based on a given operation type
    DEcouples creation from the Calculator class
    Using a dictionary mapping operation identifiers to their classes

    """

    _operations: Dict[str, type] = {
        'add' : Addition,
        'subtract' : Subtraction,
        'multiply' : Multiplication,
        'divide' : Division,
        'power' : Power,
        'root' : Root
    }

    @classmethod
    def register_operation(cls, name: str, operation_class: type) -> None:
        """
        Register a new opeartion type
        allows dynamic addition of new operations to factory
        
        ARGS:
            name (str): operation identifier (e.g. 'modulus').
            operation_class (type): The class implementing the new operation
        RAISES: 
            TypeError: if the opeartion_class DOES NOT INHERIT FROM OPERATION

        """
        if not issubclass(operation_class, Operation):
            raise TypeError("Operation class must inherit from Operation")
        cls._operations[name.lower()] = operation_class

    @classmethod
    def create_operation(cls, operation_type: str) -> Operation:
        """
        Create an operation instance based on the operation type
        THis method retrieves the appropriate operation class from the 
        _operations dictionary and instantiates it

        ARGS:
            operation_type (str): the type of operation to create e.g. add
        
        Returns:
            Operation: an instance of the specified operation class 
        Raises:
            ValueError: if the operation type is unknown

        """
        operation_class = cls._operations.get(operation_type.lower())
        if not operation_class:
            raise ValueError(f"Unknown operation: {operation_type}")
        return operation_class()
    
    