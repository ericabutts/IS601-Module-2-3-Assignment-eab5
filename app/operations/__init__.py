
class Operations:
    @staticmethod
    def add(a: float, b: float) -> float:
        """This function is used for adding two numbers. The sum of the two numbers is returned."""
        result = a + b
        return result
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """This function is used for subtracting two numbers. The difference of the two numbers is returned."""
        result = a - b
        return result
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """This function is used for multiplying two numbers. The product of the two numbers is returned."""
        result = a * b
        return result
    @staticmethod
    def divide(a: float, b: float) -> float:
        """This function is used for dividing the first number by the second. The quotient is returned.
        The ValueError will be returned if the second number is zero (0)"""
        if b==0:
            raise ValueError("Division by zero is not allowed!")
        return a / b
