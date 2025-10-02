from app.operations import Operations
# from calculator import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation # reference to function
    
    def get_result(self):
        return self.operation(self.a, self.b)
    
class CalculationFactory:
    @staticmethod
    def create_calculator(a, b, operation_name):
        operations = {
            "addition": Operations.add,
            "subtraction": Operations.subtract,
            "multiplication": Operations.multiply,
            "division": Operations.divide,
        }
        operation_function = operations.get(operation_name)
        if not operation_function:
            raise ValueError(f"Not a valid operation: {operation_name}. Input in the following format: <operation> <number 1> <number 2>")
        return Calculation(a, b, operation_function)

def calculator():
    history = []

    while True:
        userinput = input(
            "Input an operation (addition, subtraction, multiplication, division) and two numbers. Type 'help' for more details. Type 'quit' to exit: "
        )

        if userinput.lower() == "quit":
            print("Quitting program")
            break
        elif userinput.lower() == "help":
            print("""
                  Supported operations:
                    addition <num1> <num2>    : Adds two numbers
                    subtraction <num1> <num2>    : Subtracts two numbers
                    multiplication <num1> <num2>    : Multiplies two numbers
                    division <num1> <num2>    : Divides first number by second
                  Special commands:
                    help    : Shows this help message
                    history : Show all calculations performed
                    quit    : Exit the program   
                  """) # trigger help functions
        elif userinput.lower() == "history":
            if not history:
                print("No calculations have been performed.")
            for entry in history:
                print(entry)
            continue
        try:
            operation, num1, num2 = userinput.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Input is not valid. Input in the following format: <operation> <number 1> <number 2>")
            continue

        try:
            #LBYL
            if operation == "division" and num2 == 0:
                print("Division by zero is not allowed!")
                continue
            #EAFP
            calc = CalculationFactory.create_calculator(num1, num2, operation)
            result = calc.get_result()
            history.append(f"{operation} {num1} {num2} = {result}")
            print(f"{operation} result: {result}")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculator()
