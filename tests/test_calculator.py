import datetime
from pathlib import Path
import pandas as pd
import pytest
from unittest.mock import patch
from decimal import Decimal
from tempfile import TemporaryDirectory

from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.exceptions import OperationError, ValidationError
from app.history import LoggingObserver
from app.operations import OperationFactory

# ---------------------------
# Fixture for Calculator
# ---------------------------
@pytest.fixture
def calculator():
    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Create directories for logs and history
        logs_dir = temp_path / "logs"
        history_dir = temp_path / "history"
        logs_dir.mkdir(parents=True, exist_ok=True)
        history_dir.mkdir(parents=True, exist_ok=True)

        # Patch environment variables so CalculatorConfig properties return these paths
        with patch.dict("os.environ", {
            "CALCULATOR_LOG_DIR": str(logs_dir),
            "CALCULATOR_LOG_FILE": str(logs_dir / "calculator.log"),
            "CALCULATOR_HISTORY_DIR": str(history_dir),
            "CALCULATOR_HISTORY_FILE": str(history_dir / "calculator_history.csv")
        }):
            # Instantiate CalculatorConfig AFTER directories exist
            config = CalculatorConfig()
            # Ensure the log and history directories really exist (redundant but safe)
            config.log_dir.mkdir(parents=True, exist_ok=True)
            config.history_dir.mkdir(parents=True, exist_ok=True)
            
            yield Calculator(config=config)

# # ---------------------------
# # Tests
# # ---------------------------

def test_calculator_initialization(calculator):
    assert calculator.history == []
    assert calculator.undo_stack == []
    assert calculator.redo_stack == []
    assert calculator.operation_strategy is None

# def test_add_observer(calculator):
#     observer = LoggingObserver()
#     calculator.add_observer(observer)
#     assert observer in calculator.observers

# def test_remove_observer(calculator):
#     observer = LoggingObserver()
#     calculator.add_observer(observer)
#     calculator.remove_observer(observer)
#     assert observer not in calculator.observers

# def test_set_operation(calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     assert calculator.operation_strategy == operation

# def test_perform_operation_addition(calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     result = calculator.perform_operation(2, 3)
#     assert result == Decimal('5')

# def test_perform_operation_validation_error(calculator):
#     calculator.set_operation(OperationFactory.create_operation('add'))
#     with pytest.raises(ValidationError):
#         calculator.perform_operation('invalid', 3)

# def test_perform_operation_operation_error(calculator):
#     with pytest.raises(OperationError, match="No operation set"):
#         calculator.perform_operation(2, 3)

# def test_undo(calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     calculator.perform_operation(2, 3)
#     calculator.undo()
#     assert calculator.history == []

# def test_redo(calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     calculator.perform_operation(2, 3)
#     calculator.undo()
#     calculator.redo()
#     assert len(calculator.history) == 1

# @patch('app.calculator.pd.DataFrame.to_csv')
# def test_save_history(mock_to_csv, calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     calculator.perform_operation(2, 3)
#     calculator.save_history()
#     mock_to_csv.assert_called_once()

# @patch('app.calculator.pd.read_csv')
# @patch('app.calculator.Path.exists', return_value=True)
# def test_load_history(mock_exists, mock_read_csv, calculator):
#     mock_read_csv.return_value = pd.DataFrame({
#         'operation': ['Addition'],
#         'operand1': ['2'],
#         'operand2': ['3'],
#         'result': ['5'],
#         'timestamp': [datetime.datetime.now().isoformat()]
#     })
#     try:
#         calculator.load_history()
#         assert len(calculator.history) == 1
#         assert calculator.history[0].operation == "Addition"
#         assert calculator.history[0].operand1 == Decimal("2")
#         assert calculator.history[0].operand2 == Decimal("3")
#         assert calculator.history[0].result == Decimal("5")
#     except OperationError:
#         pytest.fail("Loading history failed due to OperationError")

# def test_clear_history(calculator):
#     operation = OperationFactory.create_operation('add')
#     calculator.set_operation(operation)
#     calculator.perform_operation(2, 3)
#     calculator.clear_history()
#     assert calculator.history == []
#     assert calculator.undo_stack == []
#     assert calculator.redo_stack == []
