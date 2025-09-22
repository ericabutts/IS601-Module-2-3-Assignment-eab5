import pytest
from app.operations import Operations

@pytest.mark.parametrize("a, b, expected", [
    (1,2,3),
    (4,5,6)
])
def test_addition_positive(a, b, expected):
    """Positive tests for addition"""
    assert Operations.add(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1,1,0),
    (1,2,-1),
    (1,3,-2),
])

def test_subtraction_positive(a, b, expected):
    """Positive tests for subtraction"""
    assert Operations.subtract(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1,1,1),
    (2,1,2),
    (3,1,3)
])

def test_multiplication_positive(a, b, expected):
    """Positive tests for multiplication"""
    assert Operations.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2,2,1),
    (3,3,1),
    (4,2,2),
])

def test_division_positive(a, b, expected):
    """Positive tests for division"""
    assert Operations.divide(a,b) == expected

def test_add():
    assert Operations.add(1,1) == 2

def test_subtract():
    assert Operations.subtract(1,1) == 0

def test_multiply():
    assert Operations.multiply(1,1) == 1

def test_divide_positive():
    assert Operations.divide(1,1) == 1

def test_divide_negative():
    """Test dividing by zero"""
    with pytest.raises(ValueError, match="Division by zero is not allowed!"):
        Operations.divide(1,0)