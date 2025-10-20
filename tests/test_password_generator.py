import pytest
import string
from unittest.mock import patch
from password_generator import generate_password

# --- Constants for Character Set Verification ---
VALID_CHARS = string.ascii_letters + string.digits + string.punctuation

# 1. Tests for Length

def test_password_length_default():
    """Tests that the default length of 12 generated."""
    password = generate_password()
    assert len(password) == 12

def test_password_length_custom():
    """Tests that a custom length (e.g., 20) is generated."""
    custom_length = 20
    password = generate_password(custom_length)
    assert len(password) == custom_length

def test_password_length_zero():
    """Tests that a password of length 0 is generated (edge case)."""
    password = generate_password(0)
    assert len(password) == 0
    assert password == ""

# 2. Tests for Content and Character Set

def test_password_contains_only_valid_chars():
    """Tests that all characters in the generated password are from the allowed set."""
    password = generate_password(100)
    for char in password:
        assert char in VALID_CHARS

# 3. Tests for Deterministic Output (Mocking)

@patch('random.choice')
def test_password_is_deterministic_fixed_length(mock_choice):
    """
    Mocks random.choice to ensure a fixed, predictable password is created.
    This verifies the function correctly calls random.choice 'length' times.
    """
    mock_choice.side_effect = ['a', 'B', '3', '!', 'a', 'B', '3', '!', 'a', 'B', '3', '!']

    expected_password = "aB3!aB3!aB3!"
    password = generate_password(12)

    # 1. Check the result
    assert password == expected_password

    # 2. Check the random.choice was called the correct number of times
    assert mock_choice.call_count == 12

@patch('random.choice')
def test_password_is_deterministic_custom_length(mock_choice):
    """Mocks random.choice for a different length (e.g., 5)."""
    mock_choice.side_effect = ['H', 'e', 'l', 'l', 'o']

    expected_password = "Hello"
    password = generate_password(5)

    # 1. Check the result
    assert password == expected_password

    # 2. Check that random.choice was called the correct number of times
    assert mock_choice.call_count == 5