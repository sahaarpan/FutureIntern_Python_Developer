import random
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "Hurrah!, you win!"
    else:
        return "Alas!, you lose!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose rock, paper, or scissors.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer choose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("==========================")

if __name__ == "__main__":
    play_game()
