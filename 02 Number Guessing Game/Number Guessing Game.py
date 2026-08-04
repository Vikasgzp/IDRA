import random

# Number Guessing Game

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.\n")

# Generate a random number
secret_number = random.randint(1, 100)

# Maximum attempts
max_attempts = 7

# Game loop
for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))

    if guess == secret_number:
        print(f"\n🎉 Congratulations! You guessed the correct number ({secret_number}) in {attempt} attempt(s).")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.\n")
    else:
        print("📈 Too high! Try again.\n")
else:
    print(f"\n😢 Game Over! You've used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}.")