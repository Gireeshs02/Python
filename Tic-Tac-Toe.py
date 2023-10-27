# Import necessary libraries
import os
import time

# Define global variables
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'


# Define a function to draw the board
def DrawBoard():
    """Draws the Tic-Tac-Toe board to the console."""
    print(" %c| %c| %c " % (board[1], board[2], board[3]))
    print("__|__|__")
    print(" %c| %c| %c " % (board[4], board[5], board[6]))
    print("__|__|__")
    print(" %c| %c| %c " % (board[7], board[8], board[9]))
    print("  |  | ")


# Define a function to check if a position is empty
def CheckPosition(x):
    """Checks if the specified position on the board is empty.

    Args:
        x: The position to check.

    Returns:
        True if the position is empty, False otherwise.
    """
    if board[x] == ' ':
        return True
    else:
        return False


# Define a function to check if there is a winner
def CheckWin():
    """Checks if there is a winner in the current state of the game.

        Global Variables:
            Game: The current state of the game.

        Returns:
            None
        """
    global Game
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' '
          and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


# Start the game
print("Tic-Tac-Toe Game")
print("Player 1[X] --- Player 2[O]")
print()
print()
print("Please Wait...")
time.sleep(1)

# While the game is still running
while Game == Running:
    # Clear the console
    os.system('cls')
    # Draw the board
    DrawBoard()
    # Check if it is Player 1's turn
    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
        # Get the player's choice of position
    choice = int(input("Enter position between [1-9] where you want to mark:"))
    # Check if the chosen position is empty
    if CheckPosition(choice):
        # Mark the chosen position with the player's mark
        board[choice] = Mark
        # Increment the player counter
        player += 1
        # Check if there is a winner
        CheckWin()
os.system('cls')
DrawBoard()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Player 1 Won")
    else:
        print("Player 2 Won")
