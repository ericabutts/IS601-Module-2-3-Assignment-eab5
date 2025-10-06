from app.calculation import Calculation
from app.calculator_config import CalculatorConfig

from app.exceptions import OperationError, ValidationError
from app.operations import Operation

from decimal import Decimal
from typing import Any, Dict, List, Optional, Union
Number = Union[int, float, Decimal]
CalculationResult = Union[Number, str]

from app.input_validators import InputValidator


class Calculator():
    def __init__(self, config: Optional[CalculatorConfig] = None):
        """
        Initialize Calculator with configutation
        """
        self.config = config or CalculatorConfig()
        self.operation_strategy: Optional[Operation] = None
        

    def set_operation(self, operation: Operation) -> None:
        self.operation_strategy = operation
        # logging.info(f"Set operation: {operation}")

    def perform_operation(
            self,
            a: Union[str, Number],
            b: Union[str, Number]
    ) -> CalculationResult:
        """
        """
        if not self.operation_strategy:
            raise OperationError("No operation set")
        try:
            validated_a = InputValidator.validate_number(a, self.config)
            validated_b = InputValidator.validate_number(b, self.config)
            result = self.operation_strategy.execute(validated_a, validated_b)

            calculation = Calculation(
                operation= str(self.operation_strategy),
                operand1=validated_a,
                operand2=validated_b
            )
            # Save the current state to the undo stack

            return result

        except ValidationError as e:
            # Log and re=raise validation errors
            raise
        except Exception as e:
            raise OperationError(f"Operation failed: {str(e)}")

