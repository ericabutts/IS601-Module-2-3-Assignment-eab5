import sys
from io import StringIO
import contextlib
from app.calculator import calculator  # adjust import if needed

def run_calculator_with_input(monkeypatch, inputs):
    """Simulate user input.
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

# Positive tests

def test_addition(monkeypatch):
    """Testing addition for calculator"""
    inputs = ["addition 1 1", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "addition result: 2.0" in output

def test_subtraction(monkeypatch):
    """Testing subtraction for calculator"""
    inputs = ["subtraction 1 1", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "subtraction result: 0.0" in output

def test_multiplication(monkeypatch):
    """Testing multiplication for calculator"""
    inputs = ["multiplication 1 1", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "multiplication result: 1.0" in output

def test_division(monkeypatch):
    """Testing division for calculator"""
    inputs = ["division 1 1", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "division result: 1.0" in output

#Negative Results

def test_invalid_operation(monkeypatch):
    """Test invalid input for operation"""
    inputs = ["modulus 5 3", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Not a valid operation: modulus. Input in the following format: <operation> <number 1> <number 2>" in output

def test_divide_by_zero(monkeypatch):
    """Test for invalid divide by zero"""
    inputs = ["division 1 0", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed!" in output