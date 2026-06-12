 # Real world application using control structures
# Assignment 2: E-Commerce System

def login_system():
    print("Welcome to the ShopEasy E-Commerce Platform")

    # Predefined credentials (in real app, use a database)
    users = {
        "Admin":    "admin4321",
        "Carol":    "2022carol",
        "Joy":      "joy2006",
        "CashierHope": "cash1234",
    }

    # User roles (in real app, use a database)
    roles = {
        "Admin":    "Admin",
        "Carol":    "Customer",
        "Joy":      "Customer",
        "CashierHope": "Cashier",
    }

    # Attempt to login
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if username exists
        if username in users:
            if users[username] == password:
                print("Login successful")

                # Check the role and direct to the right menu
                if roles[username] == "Admin":
                    print("Access Level: Admin - Full Access Granted")
                    admin_menu()
                elif roles[username] == "Customer":
                    print("Access Level: Customer - Limited Access Granted")
                    customer_menu()
                elif roles[username] == "Cashier":
                    print("Access Level: Cashier - Terminal Access Granted")
                    cashier_menu()

                return True
            else:
                print("Incorrect password")
        else:
            print("Username not found")

        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")

    print("Maximum login attempts reached. Access denied.")
    return False


def calculate_price():
    print("Welcome to the Price Calculator")

    # Get and validate the subtotal
    subtotal = float(input("Enter the product subtotal ($): "))

    # Check discount level based on subtotal amount
    if subtotal >= 500:
        auto_discount_rate = 0.15
        print("Bulk discount applied: 15%")
    elif subtotal >= 200:
        auto_discount_rate = 0.10
        print("Loyalty discount applied: 10%")
    elif subtotal >= 100:
        auto_discount_rate = 0.05
        print("Standard discount applied: 5%")
    else:
        auto_discount_rate = 0.0
        print("No automatic discount")

    auto_discount_amount = subtotal * auto_discount_rate

    # Check coupon code
    # Predefined coupon codes (in real app, use a database)
    coupon_codes = {
        "SAVE10":  0.10,
        "WELCOME": 0.15,
        "FLASH20": 0.20,
    }

    coupon_discount_amount = 0.0
    coupon_input = input("Enter a coupon code (or press Enter to skip): ").upper()

    if coupon_input == "":
        print("No coupon code entered")
    elif coupon_input in coupon_codes:
        coupon_discount_amount = subtotal * coupon_codes[coupon_input]
        print("Coupon code applied: " + str(int(coupon_codes[coupon_input] * 100)) + "% off")
    else:
        print("Invalid coupon code")

    price_after_discount = subtotal - auto_discount_amount - coupon_discount_amount

    # Check tax rate based on location
    print("Select your location:")
    print("1. New York    (8.875%)")
    print("2. California  (7.250%)")
    print("3. Texas       (6.250%)")
    print("4. International / Tax-Exempt (0%)")

    location_choice = input("Enter location number (1-4): ")

    if location_choice == "1":
        tax_rate = 0.08875
        print("Tax rate: 8.875% (New York)")
    elif location_choice == "2":
        tax_rate = 0.0725
        print("Tax rate: 7.25% (California)")
    elif location_choice == "3":
        tax_rate = 0.0625
        print("Tax rate: 6.25% (Texas)")
    elif location_choice == "4":
        tax_rate = 0.0
        print("Tax rate: 0% (International / Tax-Exempt)")
    else:
        tax_rate = 0.0
        print("Invalid location. Defaulting to 0% tax")

    tax_amount = price_after_discount * tax_rate
    final_price = price_after_discount + tax_amount

    # Print the order summary
    print("Order Summary:")
    print("Subtotal: $" + str(round(subtotal, 2)))
    print("Auto Discount: -$" + str(round(auto_discount_amount, 2)))
    print("Coupon Discount: -$" + str(round(coupon_discount_amount, 2)))
    print("Tax: +$" + str(round(tax_amount, 2)))
    print("Final Price: $" + str(round(final_price, 2)))

    return True


def admin_menu():
    print("Admin Menu:")
    print("1. Calculate Price")
    print("2. View All Users")
    print("3. Manage Inventory")
    print("4. View Sales Reports")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("Displaying all users")
    elif choice == "3":
        print("Opening inventory manager")
    elif choice == "4":
        print("Generating sales report")
    else:
        print("Invalid option")


def customer_menu():
    print("Customer Menu:")
    print("1. Calculate My Order Price")
    print("2. View My Order History")

    choice = input("Select an option (1-2): ")

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("Displaying your order history")
    else:
        print("Invalid option")


def cashier_menu():
    print("Cashier Menu:")
    print("1. Process a New Order")
    print("2. View Today's Transactions")

    choice = input("Select an option (1-2): ")

    if choice == "1":
        calculate_price()
    elif choice == "2":
        print("Displaying today's transactions")
    else:
        print("Invalid option")


login_system()