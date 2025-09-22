import sys
from io import StringIO
import contextlib
from app.calculator import calculator  # adjust import if needed
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
    assert "Not a valid operation: modulus. Input in the following format: <operation> <number 1> <number 2>" in output

def test_divide_by_zero(monkeypatch):
    """Test for invalid divide by zero"""
    inputs = ["division 1 0", "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed!" in output

@pytest.mark.parametrize("user_input, expected_output", [
    ("addition 0 5", "addition result: 5.0"),
    ("subtraction -3 7", "subtraction result: -10.0"),
    ("multiplication 2.5 3.5", "multiplication result: 8.75"),
    ("division 10000000 1000", "division result: 1000.0"),
])

def test_edge_cases(monkeypatch, user_input, expected_output):
    inputs = [user_input, "quit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert expected_output in output