import sys
from io import StringIO
import contextlib
from app.calculator import calculator, CalculationFactory, Calculation  # adjust import if needed
import pytest

def run_calculator_with_input(monkeypatch, inputs):
    """Simulating user input.
    param monkeypatch: pytest fixture to simulate user input
    param inputs: list of strings representing simulated input
    return: captured output as a string
    """

    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    capture_output = StringIO()
    with contextlib.redirect_stdout(capture_output):
        calculator()

    return capture_output.getvalue()

# Test creation of Calculator for full coverage

@pytest.mark.parametrize("a, b, op_name, expected", [
    (2, 3, "addition", 5),
    (10, 4, "subtraction", 6),
    (3, 5, "multiplication", 15),
    (8, 2, "division", 4),
])
def test_create_calculator_valid(a, b, op_name, expected):
    calc = CalculationFactory.create_calculator(a, b, op_name)
    assert isinstance(calc, Calculation)
    assert calc.get_result() == expected

@pytest.mark.parametrize("a, b, op_name", [
    (2, 3, "modulus"),
    (1, 1, "power"),
    (5, 2, "sqrt"),
])
def test_create_calculator_invalid(a, b, op_name):
    with pytest.raises(ValueError) as excinfo:
        CalculationFactory.create_calculator(a, b, op_name)
    assert f"Not a valid operation: {op_name}" in str(excinfo.value)

# Positive tests

@pytest.mark.parametrize("commands", [(["help", "quit"]),])

def test_help_command(monkeypatch, commands):
    """Test the help command prints instructions for using the program."""
    expected_strings = [
        "Supported operations:",
        "addition <num1> <num2>",
        "subtraction <num1> <num2>",
        "multiplication <num1> <num2>",
        "division <num1> <num2>",
        "Special commands:",
        "help",
        "history",
        "quit",
    ]
    output = run_calculator_with_input(monkeypatch, commands)

    for expected in expected_strings:
        assert expected in output

@pytest.mark.parametrize("commands, expected_entries", [
    (["addition 1 1","history","quit"], ["addition 1.0 1.0 = 2.0"]),    
    (["subtraction 5 2","multiplication 3 4","history","quit"], 
     ["subtraction 5.0 2.0 = 3.0", "multiplication 3.0 4.0 = 12.0"]),    
])

def test_history_command(monkeypatch, commands, expected_entries):
    output = run_calculator_with_input(monkeypatch, commands)

    for entry in expected_entries:
        assert entry in output

@pytest.mark.parametrize("user_input, expected_output", [
    ("addition 1 1", "addition result: 2.0"),
    ("subtraction 1 1", "subtraction result: 0.0"),
    ("multiplication 1 1", "multiplication result: 1.0"),
    ("division 1 1", "division result: 1.0"),
])
def test_operations(monkeypatch, user_input, expected_output):
    """Testing all basic operations with parameterized inputs"""
    inputs = [user_input, "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert expected_output in output


#Negative Results

@pytest.mark.parametrize("user_input", [
    "add 1 1 1", 
    "subtract 1",
    "multiply a b",
    "division 1 c",
])

def test_invalid_inputs(monkeypatch, user_input):
    """Test an invalid amount of inputs"""
    inputs = [user_input, "quit"]
    outputs = run_calculator_with_input(monkeypatch, inputs)
    assert "Input is not valid. Input in the following format: <operation> <number 1> <number 2>" in outputs

@pytest.mark.parametrize("user_input", [
    "modulus 5 3",
    "power 2 3",
    "sqrt 4 2"
])

def test_invalid_operation(monkeypatch, user_input):
    """Test invalid input for an  operation"""
    inputs = [user_input, "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    operation = user_input.split()[0]
    assert f"Not a valid operation: {operation}. Input in the following format: <operation> <number 1> <number 2>" in output

def test_divide_by_zero(monkeypatch):
    """Test for invalid divide by zero"""
    inputs = ["division 1 0", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed!" in output

@pytest.mark.parametrize("user_input, expected_output", [
    ("addition 0 5", "addition result: 5.0"),
    ("subtraction -3 7", "subtraction result: -10.0"),
    ("multiplication 2.5 3.5", "multiplication result: 8.75"),
    ("division 10000000 1000", "division result: 10000.0"),
])

def test_edge_cases(monkeypatch, user_input, expected_output):
    inputs = [user_input, "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert expected_output in output
    