"""A simple calculator supporting four arithmetic operations."""


def calculate(a, b, operation):
    """Calculate using addition, subtraction, multiplication, or division."""
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")

    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        raise ValueError("Unsupported operation. Use +, -, *, or /.")


def main():
    print("Python Calculator")
    print("Supported operations: +, -, *, /")
    print("Type 'exit' to quit.")

    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()

        if operation.lower() == "exit":
            print("Goodbye!")
            break

        if operation not in ("+", "-", "*", "/"):
            print("Error: Unsupported operation. Use +, -, *, or /.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = calculate(a, b, operation)
            print("Result:", result)
        except (ValueError, TypeError, ZeroDivisionError) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
