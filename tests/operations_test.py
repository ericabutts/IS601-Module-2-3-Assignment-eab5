import pytest
from app.operations import add, subtract, multiply, divide

def test_add():
    assert add(1,1) == 2

def test_subtract():
    assert subtract(1,1) == 0

def test_multiply():
    assert multiply(1,1) == 1

def test_divide_positive():
    assert divide(1,1) == 1

def test_divide_negative():
    """Test dividing by zero"""
    with pytest.raises(ValueError, match="Division by zero is not allowed!"):
        divide(1,0)