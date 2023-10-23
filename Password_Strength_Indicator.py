import re


def check_password_strength(password):
    """"Checks the strength of a password.

  Args:
    password: A string containing the password to check.

  Returns:
    A string indicating the password strength, one of the following:
    * "Weak"
    * "Medium"
    * "Strong"
    """

    # Check if the password is at least 5 characters long.
    if len(password) <= 5:
        return "Weak"

    # Check if the password is at least 8 characters long.
    if len(password) <= 8:
        return "Medium"

    # Check if the password contains at least one uppercase letter.
    if not re.search(r'[A-Z]', password):
        return "Medium"

    # Check if the password contains at least one lowercase letter.
    if not re.search(r'[a-z]', password):
        return "Medium"

    # Check if the password contains at least one digit.
    if not re.search(r'\d', password):
        return "Medium"

    # Check if the password contains at least one special character.
    if not re.search(r'[! @#$%^&*(),.?":{}|<>]', password):
        return "Medium"

    # If all of the above conditions are met, the password is strong.
    return "Strong"


# Prompt the user for a password.
password = input("Enter a password: ")

# Check the password strength and print the result.
password_strength = check_password_strength(password)
print(f"Your password strength is: {password_strength}")
