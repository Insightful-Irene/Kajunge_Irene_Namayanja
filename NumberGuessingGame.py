print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 10")

secret_number = 7

chances = 3
guess_count = 0

while guess_count < chances:
    guess = int(input("Enter your guess: "))
    guess_count = guess_count + 1

    if guess == secret_number:
        print("Correct! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    remaining = chances - guess_count
    if remaining > 0:
        print("Chances left:", remaining)

if guess != secret_number:
    print("You ran out of chances.")
    print("The correct number was:", secret_number)