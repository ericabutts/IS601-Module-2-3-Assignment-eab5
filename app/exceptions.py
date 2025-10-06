### Exception Hierarchy ###

class CalculatorError(Exception):
    """
    Base exception class for calculator specific errors
    All custom exceptions for the calculator application inherit from this class
    allowed for unified error handling
    """
    pass

class ValidationError(CalculatorError):
    """
    Raised when input valiation fails
    This exception is triggered when a user inputs do not meet the required criteria,
    such as entering non-numberic values or exceeding maximum characters
    which might depend on the operation
    """
    pass

class OperationError(CalculatorError):
    """Raised when a calculation operation fails
    This exception is used to indicate failures during exection of 
    arithmetic operations such as division by zero or invlaid operations
    """
    pass

class ConfigurationError(CalculatorError):
    """Raised when a configuration issue arises"""
    pass