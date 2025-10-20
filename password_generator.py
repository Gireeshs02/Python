import string
import random

def generate_password(length=12):
    """Generate a random password with letters, digits, and symbols."""

    # Define character set (letters + digits + punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Example usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated password:", password)
