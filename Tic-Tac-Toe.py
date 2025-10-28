# Import necessary libraries
import os
import time

# Define global variables
INITIAL_BOARD = [' '] * 10
WIN = 1
DRAW = -1
RUNNING = 0
PLAYER_MARKS = {1: 'X', 2: 'O'}

# Define a function to check if a position is empty
def check_position(board: list, x: int) -> bool:
    """Checks if the specified position on the board is empty.

    Args:
        board: The current game board list.
        x: The position to check (1-9).

    Returns:
        True if the position is empty and valid (1-9), False otherwise.
    """
    if 1 <= x <= 9 and board[x] == ' ':
        return True
    return False


# Define a function to check if there is a winner
def check_win(board: list) -> int:
    """Checks if there is a winner or a draw in the current state of the game.

    Args:
        board: The current game board list.

    Returns:
        int: WIN (1), DRAW (-1), or RUNNING (0).
    """
    # Check all 8 winning combinations
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)             # Diagonal
    ]

    for a, b, c in winning_combinations:
        # Check if all three positions are marked by the same player (and not empty)
        if board[a] != ' ' and board[a] == board[b] and board[b] == board[c]:
            return WIN  # A player has won
        
    # Check for Draw (if no winner and no empty spaces)
    # Check only board indices 1 through 9
    if ' ' not in board[1:]:
        return DRAW

    # Game is still ongoing
    return RUNNING

# Define a function to draw the board
def draw_board(board: list):
    """Draws the Tic-Tac-Toe board to the console."""
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("---|---|---")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("---|---|---")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

def run_game_loop():
    """Manages the main game flow."""
    board = list(INITIAL_BOARD)
    current_player_num = 1
    game_state = RUNNING

    print("Tic-Tac-Toe Game")
    print(f"Player 1[{PLAYER_MARKS[1]}] --- Player 2[{PLAYER_MARKS[2]}]")
    print("Board Positions: 1-9")
    time.sleep(1)

    while game_state == RUNNING:
        try:
            os.system('cls')
            draw_board(board)
            
            mark = PLAYER_MARKS[current_player_num]
            
            print(f"Player {current_player_num}'s chance ({mark})")
            
            choice = int(input("Enter position between [1-9] where you want to mark: "))
            
            if check_position(board, choice):
                board[choice] = mark
                
                # Check for win/draw after the move
                game_state = check_win(board)
                
                # Only switch player if the game is still running
                if game_state == RUNNING:
                    current_player_num = 2 if current_player_num == 1 else 1
            else:
                print("Invalid move or position taken. Try again.")
                time.sleep(1)

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            time.sleep(1)
        except IndexError:
            # Should not happen if _check_position is working, but safe to include
            print("Position must be between 1 and 9.")
            time.sleep(1)

    # Game Over
    os.system('cls')
    draw_board(board)

    if game_state == DRAW:
        print("Game Draw!")
    elif game_state == WIN:
        # The winner is the player who just made the last valid move
        print(f"Player {current_player_num} Won!")

if __name__ == "__main__":
    run_game_loop()
