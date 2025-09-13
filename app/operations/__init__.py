


def add(a: float, b: float) -> float:
    result = a + b
    return result

def subtract(a: float, b: float) -> float:
    result = a - b
    return result

def multiply(a: float, b: float) -> float:
    result = a * b
    return result

def divide(a: float, b: float) -> float:
    if b==0:
        raise ValueError("Division by zero is not allowed!")
    return a / b
