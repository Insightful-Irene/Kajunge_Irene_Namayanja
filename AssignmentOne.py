#Bill Split Clculator
bill = float(input("Enter the total bill amount: shs"))
people = int(input("Enter the number of people: "))

print("Choose digit for a tip percentage")
print("1 for 10%")
print("2 for 15%")
print("3 for20%")
print("4 for Custom")
choice = input("Enter your choice (1, 2, 3, or 4): ")

if choice == "1":
    tipPercent = 10
elif choice == "2":
    tipPercent = 15
elif choice == "3":
    tipPercent = 20
elif choice == "4":
    tipPercent = float(input("Enter your custom tip percentage: "))
else:
    print("Invalid choice,tip percentage does not exist")
    

tipAmount = bill * (tipPercent / 100)
totalBill = bill + tipAmount
perPerson = totalBill / people

print()
print(" RECEIPT")
print(f"Original bill:    shs{bill:.2f}")
print(f"People:           {people}")
print(f"Tip given in percent         ({tipPercent}%)")
print(f"Tip given in cash(Ug.shs)     shs{tipAmount:.2f}")
print(f"Total bill with tips :       shs{totalBill:.2f}")
print(f"Each person pays: shs{perPerson:.2f}")

