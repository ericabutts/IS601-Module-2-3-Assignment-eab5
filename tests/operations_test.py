import pytest
from app.operations import Operations

@pytest.mark.parametrize("a, b, expected", [
    (1,2,3),
    (4,5,9),
    (0,5,5),         
    (-2,3,1),         
    (2.5, 3.5, 6.0)], ids=[
    "positive_numbers",
    "positive_numbers2",
    "zero_and_positive",
    "negative_and_positive",
    "float_numbers"
]
    )
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

@pytest.mark.parametrize("a, b", [
    (1, 0),
    (-1, 0),
    (0, 0),
])

def test_divide_by_zero(a, b):
    """Test dividing by zero"""
    with pytest.raises(ValueError, match="Division by zero is not allowed!"):
        Operations.divide(a,b)