from app.operations import Operations
# from calculator import add, subtract, multiply, divide

def calculator():
    while True:
        userinput = input(
            "Input an operation (addition, subtraction, multiplication, division) and two numbers. Type 'quit' to exit: "
        )

        if userinput.lower() == "quit":
            print("Quitting program")
            break

        try:
            operation, num1, num2 = userinput.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Input is not valid. Input in the following format: <operation> <number 1> <number 2>")
            continue

        try:
            if operation == "addition":
                result = Operations.add(num1, num2)
            elif operation == "subtraction":
                result = Operations.subtract(num1, num2)
            elif operation == "multiplication":
                result = Operations.multiply(num1, num2)
            elif operation == "division":
                result = Operations.divide(num1, num2)
            else:
                print(f"Not a valid operation: {operation}. Input in the following format: <operation> <number 1> <number 2>")
                continue

            print(f"{operation} result: {result}")

        except ValueError as e:
            print(e)
