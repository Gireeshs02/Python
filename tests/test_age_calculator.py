import pytest
from age_calculator import calculate_age

# --- 1. Happy Path Tests (using a fixed 'today' date for mental calculation) ---
# We know that 'calculate_age' will use the actual system date (today is 2025-10-11).
# We test a recent age and an older age to ensure the logic works.

def test_age_calculation_passed_birthday():
    """Test when the birthday has already passed this year (e.g., May 15)."""
    # Assuming today is 2025-10-11
    # Birthdate: 1990-05-15 (Expected Age: 35)
    result = calculate_age('1990-05-15')
    assert result == 35

def test_age_calculation_yet_to_pass_birthday():
    """Test when the birthday is later this year (e.g., December 25)."""
    # Assuming today is 2025-10-11
    # Birthdate: 1990-12-25 (Expected Age: 34)
    result = calculate_age('1990-12-25')
    assert result == 34

def test_age_calculation_on_birthday():
    """Test when the birthday is exactly today (2025-10-11)."""
    # Birthdate: 1990-10-11 (Expected Age: 35)
    result = calculate_age('1990-10-11')
    assert result == 35

def test_age_calculation_zero_years():
    """Test a very recent birthdate (age 0)."""
    # Birthdate: 2025-01-01 (Expected Age: 0)
    result = calculate_age('2025-01-01')
    assert result == 0

# --- 2. Input Validation and Error Tests ---

def test_invalid_date_format_raises_error():
    """Test that an incorrect date string format raises an error."""
    # pytest.raises checks that the expected exception is raised
    with pytest.raises(ValueError, match="time data '15-05-1990' does not match format '%Y-%m-%d'"):
        calculate_age('15-05-1990')

def test_unrealistic_age_raises_error():
    """Test the custom validation for ages over 150."""
    # Birth year 1800 (age 225)
    with pytest.raises(ValueError, match="Unrealistic age. Please enter a valid birth year."):
        calculate_age('1800-01-01')

def test_empty_string_raises_error():
    """Test that passing an empty string raises an error."""
    with pytest.raises(ValueError, match="time data '' does not match format '%Y-%m-%d'"):
        calculate_age('')