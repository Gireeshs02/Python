import random

CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors"}

def get_choice(choice_num):
    return CHOICES.get(choice_num, None)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "win"
    else:
        return "loss"

def get_user_choice():
    while True:
        try:
            user_input = int(input("Enter your choice (1=Rock, 2=Paper, 3=Scissors, 0=Quit): "))
            if user_input == 0:
                return None
            choice = get_choice(user_input)
            if choice:
                return choice
            else:
                print("Invalid choice! Please enter 0, 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game():
    print("\n--- Rock, Paper, Scissors ---")
    results = {"win": 0, "loss": 0, "tie": 0}

    while True:
        user_choice = get_user_choice()
        if user_choice is None:  # Quit selected
            break

        computer_choice = get_choice(random.randint(1, 3))

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        outcome = determine_winner(user_choice, computer_choice)

        if outcome == "win":
            print("You win this round!")
            results["win"] += 1
        elif outcome == "loss":
            print("Computer wins this round!")
            results["loss"] += 1
        else:
            print("It's a tie!")
            results["tie"] += 1

    print("\n--- Game Summary ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Ties: {results['tie']}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
