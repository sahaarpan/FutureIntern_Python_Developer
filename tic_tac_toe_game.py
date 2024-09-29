def print_board(board):
    """Prints the current state of the board."""
    print("\n".join([" | ".join(row) for row in board]))
    print("\n")


def check_winner(board, player):
    """Checks if the current player has won."""
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions


def is_draw(board):
    """Checks if the board is full and the game is a draw."""
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    """Main function to play the Tic Tac Toe game."""
    while True:
        # Initialize the board
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'
        game_over = False

        while not game_over:
            print_board(board)
            print(f"Player {current_player}'s turn.")

            # Get valid move from the player
            while True:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    if board[row][col] == ' ':
                        board[row][col] = current_player
                        break
                    else:
                        print("Cell is already taken. Try again.")
                except (IndexError, ValueError):
                    print("Invalid input. Please enter numbers between 0 and 2.")

            # Check for a winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True
            else:
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'

        # Ask if players want to restart or exit
        while True:
            restart = input("Do you want to play again? (yes/no): ").strip().lower()
            if restart in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if restart == 'no':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
