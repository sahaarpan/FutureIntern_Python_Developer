import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Please choose a number between 1 and 100.")

    while True:
        try:
            # Ask the user for their guess
            number_guessed = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if number_guessed < number_to_guess:
                print("Too low! Try again.")
            elif number_guessed > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    guess_the_number()
