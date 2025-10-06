from decimal import Decimal
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.operations import OperationFactory

def calculator_repl():
    """
    Command line interface for calculator usage
    """
    calc = Calculator()
    print("Calculator REPL started. Type 'help' for commands, 'quit' to exit.")

    while True:
        try:
            command = input("\nEnter command: ").lower().strip()

            if command in ['quit', 'exit']:
                print("Exiting calculator.")
                break

            if command == 'help':
                print("\nAvailable commands:")
                print(" add, subtract, multiply, divide, power, root")
                print(" cancel → cancels current operation")
                print(" quit/exit → exit program")
                continue

            if command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root']:
                print("\nEnter numbers (or type 'cancel' to abort):")

                a = input("First number: ")
                if a.lower() == 'cancel':
                    print("Operation cancelled")
                    continue

                b = input("Second number: ")
                if b.lower() == 'cancel':
                    print("Operation cancelled")
                    continue

                operation = OperationFactory.create_operation(command)
                calc.set_operation(operation)

                # perform calculation
                result = calc.perform_operation(a, b)
                if isinstance(result, Decimal):
                    result = result.normalize()
                print(f"\nResult: {result}")

                continue

            # unknown command
            print("Unknown command. Type 'help' for available commands.")

        except (ValidationError, OperationError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Fatal error: {e}")
            raise
