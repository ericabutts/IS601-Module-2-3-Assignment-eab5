import pytest
from app.operations import add, subtract, multiply, divide

def test_addition_positive():
    """Positive tests for addition"""
    assert add(1,2) == 3
    assert add(1,3) == 4
    assert add(1,4) == 5

# def test_addition_negative():
#     """Negative tests for addition"""
#     assert add(1,2) == 0
#     assert add(1,3) == 0
#     assert add(1,4) == 0

def test_subtraction_positive():
    """Positive tests for subtraction"""
    assert subtract(1,1) == 0
    assert subtract(1,2) == -1
    assert subtract(1,3) == -2

# def test_subtraction_negative():
#     """Negative tests for subtraction"""
#     assert subtract(1,1) == 1
#     assert subtract(1,2) == 1
#     assert subtract(1,3) == 1

def test_multiplication_positive():
    """Positive tests for multiplication"""
    assert multiply(1,1) == 1
    assert multiply(1,2) == 2
    assert multiply(1,3) == 3

# def test_multiplication_negative():
#     """Negative tests for multiplication"""
#     assert multiply(1,5) == 6
#     assert multiply(2,5) == 12
#     assert multiply(4,4) == 15

def test_division_positive():
    """Positive tests for division"""
    assert divide(1,1) == 1
    assert divide(2,1) == 2
    assert divide(12,2) == 6

# def test_division_negative():
#     """Negative tests for division"""
#     assert divide(3, 2) == 0
#     assert divide(4,2) == 3
#     assert divide(2,2) == 2

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