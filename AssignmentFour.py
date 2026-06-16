# Calculator program using functions for basic arithmetic operations

def add(a, b):
    # Returns the sum of two numbers
    return a + b

def subtract(a, b):
    # Returns the difference between two numbers
    return a - b

def multiply(a, b):
    # Returns the product of two numbers
    return a * b

def divide(a, b):
    # Returns the quotient of two numbers
    # Guards against division by zero error
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():
    # Prompts the user to enter two numbers and returns them as floats
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def calculator():
    # Main function that displays the menu and handles user choices
    # Loops continuously until the user selects Exit (option 5)
    while True:
        print("\n CALCULATOR MENU ")
        print(" select 1 for Addition")
        print(" select 2 for Subtraction")
        print(" select 3 for  Multiplication")
        print("select 4 for Division")
        print("select 5 for Exit")
        print(" ")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            # Get numbers and call the add function
            a, b = get_numbers()
            print(f"Result: {a} + {b} = {add(a, b)}")

        elif choice == '2':
            # Get numbers and call the subtract function
            a, b = get_numbers()
            print(f"Result: {a} - {b} = {subtract(a, b)}")

        elif choice == '3':
            # Get numbers and call the multiply function
            a, b = get_numbers()
            print(f"Result: {a} * {b} = {multiply(a, b)}")

        elif choice == '4':
            # Get numbers and call the divide function
            a, b = get_numbers()
            print(f"Result: {a} / {b} = {divide(a, b)}")

        elif choice == '5':
            # Exit the program when user is done
            print("Goodbye!")
            break

        else:
            # Handle any invalid menu input
            print("Invalid option. Please choose 1-5.")

# Run the calculator
calculator()