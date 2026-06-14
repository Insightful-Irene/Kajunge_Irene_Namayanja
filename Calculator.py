print("Simple Calculator")

running = True

while running:
    print("Choose an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Goodbye!")
        running = False

    elif choice == "1" or choice == "2" or choice == "3" or choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print("Answer:", result)

        elif choice == "2":
            result = num1 - num2
            print("Answer:", result)

        elif choice == "3":
            result = num1 * num2
            print("Answer:", result)

        elif choice == "4":
            if num2 == 0:
                print("You cannot divide by zero.")
            else:
                result = num1 / num2
                print("Answer:", result)

    else:
        print("Invalid choice. Try again.")