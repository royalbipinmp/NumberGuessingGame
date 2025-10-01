import random
# Generate a random number between 1 and 100
number=random.randint(1, 100)
attempts=0
guess=0
print("Welcome to the Number Guessing Game!")
# Loop until the user guesses the correct number
while guess != number:
    guess = int(input("Enter your guess:"))
    attempts += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")