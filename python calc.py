def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_user_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Select operation (+, -, *, /): ")
    return num1, num2, operation

def main():
    try:
        num1, num2, operation = get_user_input()
        if operation == "+":
            print(num1, "+", num2, "=", add(num1, num2))
        elif operation == "-":
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif operation == "*":
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif operation == "/":
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

  ## WHAT TO KNOW ABOUT THIS  PIECES OF CODES:

## (1) . Function definitions
## add(x, y): Returns the sum of x and y.
## subtract(x, y): Returns the difference between x and y.
## multiply(x, y): Returns the product of x and y.
## divide(x, y): Returns the quotient of x and y. If y is 0, it raises a ValueError as division by zero is undefined.

## (2). get_user_input() function:
## Prompts the user to enter the first number (num1).
## Prompts the user to enter the second number (num2).
## Prompts the user to select an operation (+, -, *, /).
## Returns the tuple (num1, num2, operation).

## (3) . main() function:
## Calls get_user_input() to get the user's input.
## Performs the selected arithmetic operation based on the operation symbol.
## Catches ValueError exceptions raised by the divide() function if the second number is 0.
## Catches any other exceptions that might occur during the execution of the program.
## Prints the result of the arithmetic operation or an error message if an exception is caught.

## (4). The script checks if __name__ is equal to "__main__", which is true if the script is run directly. 
## If this condition is met, it calls the main() function to start the execution of the program.
