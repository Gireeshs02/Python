from datetime import date, datetime

def calculate_age(birthdate: str) -> int:
    """
    Calculate age in years from the given birthdate.
    
    Args:
        birthdate (str): Date of birth in 'YYYY-MM-DD' format.
    
    Returns:
        int: Age in years.
    """

    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
        today = date.today()

        if birth_date > today:
            raise ValueError("Birthdate cannot be in the future.")
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        if age < 0 or age > 150:
            raise ValueError("Unrealistic age. Please enter a valid birth year.")
        
        return age
    
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == "__main__":
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        age = calculate_age(dob)
        print(f"Your age is: {age}")

    except ValueError as e:
        print(f"Error: {e}")