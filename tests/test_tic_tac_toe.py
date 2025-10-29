import pytest

# Import functions and constants from the refactored module
from tic_tac_toe import check_win, check_position, WIN, DRAW, RUNNING

# --- Constants for Test Board Setup ---
X = 'X'
O = 'O'
E = ' ' # E for Empty

# Create a clean, immutable board list template
EMPTY_BOARD = [E] * 10 

# ----------------------------------------------------
# 1. Tests for _check_position(board, x)
# ----------------------------------------------------

def test_check_position_empty():
    """Should return True if position 5 is empty."""
    assert check_position(EMPTY_BOARD, 5) == True

def test_check_position_occupied():
    """Should return False if position 3 is occupied by 'X'."""
    board_occupied = list(EMPTY_BOARD)
    board_occupied[3] = X
    assert check_position(board_occupied, 3) == False

@pytest.mark.parametrize("position", [0, 10, -1])
def test_check_position_out_of_bounds(position):
    """Should return False for positions outside the valid 1-9 range."""
    # Note: The function handles index bounds checking explicitly (1 <= x <= 9)
    assert check_position(EMPTY_BOARD, position) == False

# ----------------------------------------------------
# 2. Tests for check_win(board) - All Win/Draw/Running Conditions
# ----------------------------------------------------

@pytest.mark.parametrize("winning_board", [
    # Horizontal Wins (1, 2, 3), (4, 5, 6), (7, 8, 9)
    [E, X, X, X, E, E, E, E, E, E], 
    [E, E, E, E, O, O, O, E, E, E], 
    [E, E, E, E, E, E, E, X, X, X], 

    # Vertical Wins (1, 4, 7), (2, 5, 8), (3, 6, 9)
    [E, X, E, E, X, E, E, X, E, E], 
    [E, E, O, E, E, O, E, E, O, E], 
    [E, E, E, O, E, E, O, E, E, O],

    # Diagonal Wins (1, 5, 9), (3, 5, 7)
    [E, X, E, E, E, X, E, E, E, X], 
    [E, E, E, O, E, O, E, O, E, E], 
])
def test_check_win_wins(winning_board):
    """Tests all standard winning scenarios."""
    assert check_win(winning_board) == WIN

def test_check_win_running_empty():
    """Should return RUNNING for an empty board."""
    assert check_win(EMPTY_BOARD) == RUNNING

def test_check_win_running_partial():
    """Should return RUNNING for a board with moves but no win/draw."""
    board_partial = [E, X, E, O, E, E, X, E, E, O]
    assert check_win(board_partial) == RUNNING

def test_check_win_draw():
    """Tests a full board where no one has won (Draw)."""
    # The board state is: X O X / O X X / O X O
    draw_board = [' ', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O']
    assert check_win(draw_board) == DRAW

def test_check_win_full_but_running_false():
    """Ensures that a full board always results in a WIN or DRAW, never RUNNING."""
    board_full_draw = [' ', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X', 'O']
    
    result = check_win(board_full_draw)
    assert result != RUNNING
    assert result == DRAW
