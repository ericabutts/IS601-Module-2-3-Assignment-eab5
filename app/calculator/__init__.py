from app.operations import add, subtract, multiply, divide

def calculator():
        
    while True:
        userinput = input("Input an operation (addition, subtraction, multiplication, division) and two numbers. Type 'quit' to exit")
        print(userinput)

        if (userinput.lower()=="quit"):
            print("Quitting program")
            break

        try:
            operation, num1, num2 = userinput.split()
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Input is not valid. Input in the following format: <operation> <number 1> <number 2>")
            continue

        if (operation=="addition"):
            result = add(num1, num2)
            print(f"addition result: {result}")
        elif (operation=="subtraction"):
            result = subtract(num1, num2)
            print(f"subtraction result: {result}")
        elif (operation=="multiplication"):
            result = multiply(num1, num2)
            print(f"multiplication result: {result}")
        elif (operation=="division"):
            result = divide(num1, num2)
            print(f"division result: {result}")
        else:
            print(f"Not a valid operation: {operation}. Input in the following format: <operation> <number 1> <number 2>")
            continue