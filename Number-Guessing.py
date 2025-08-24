import random as rd

def guess_number():
    print("Welcome to Number Guessing Game!")

    print("\nChoose difficulty:")
    print("1. Easy (10 chances)")
    print("2. Medium (7 chances)")
    print("3. Hard (5 chances)")

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3):"))
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please choose 1 or 2 or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (1/2/3).")

    if choice == 1:
        secret_num = rd.randint(1, 100)
        max_attempts = 10
    elif choice == 2:
        secret_num = rd.randint(1, 100)
        max_attempts = 7
    elif choice == 3:
        secret_num = rd.randint(1, 100)
        max_attempts = 5

    attempts = 0

    while True:
        try:
            num = int(input("Enter your guess number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if num == secret_num:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif num > secret_num:
            print("The number is too high.")
        elif num < secret_num:
            print("The number is too low.")

        if max_attempts and attempts >= max_attempts:
            print(f"You've reached maximum attempts. The number was {secret_num}.")
            break

    again = input("Do you want to play again? (y/n): ").lower()
    if again == "y":
        guess_number()
    else:
        print("Thanks for playing!!")

if __name__ == "__main__":
    guess_number()
