import random

def guess_number():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number within the range {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
