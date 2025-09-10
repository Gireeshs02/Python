ROWS = 5
COLS = 7

seats = [[0 for _ in range(COLS)] for _ in range(ROWS)]

def viewSeats():
    print("\n--- Seat Layout (0 = Available, 1 = Booked) ---")
    for i in range(ROWS):
        for j in range(COLS):
            print(seats[i][j], end = " ")
        print()

def bookSingleSeat():
    try:
        r, c = map(int, input("\nEnter row and column to book (e.g., 2 3): ").split(' '))
    
        if 0 <= r < ROWS and 0 <= c < COLS and seats[r][c] == 0:
            seats[r][c] = 1
            print("\nSeat booked successfully.")
        else:
            print("\nInvalid or Seat already booked.")
    except ValueError:
        print("\nPlease enter valid numbers (row col).")

def bookMultipleSeats():
    try:
        r, c, count = map(int, input("\nEnter row, col and number of seats to book: ").split(' '))

        if 0 <= r < ROWS and 0 <= c < COLS and c + count <= COLS:
            canBook = True

            for i in range(count):
                if seats[r][c + i] == 1:
                    canBook = False
                    break

            if canBook:
                for i in range(count):
                    seats[r][c + i] = 1
                print("\nMultiple seats booked successfully.")
            else:
                print("\nOne or more seats already booked in this block.")
        else:
            print("\nInvalid row or seat range.")
    except ValueError:
        print("\nPlease enter valid numbers (row col count).")

def cancelSeat():
    try:
        r, c = map(int, input("\nEnter row and column to cancel: ").split(' '))
    
        if 0 <= r < ROWS and 0 <= c < COLS and seats[r][c] == 1:
            seats[r][c] = 0
            print("\nBooking cancelled.")
        else:
            print("\nInvalid seat or not booked.")
    except ValueError:
        print("\nPlease enter valid numbers (row col).")

def displayAvailableSeats():
    print("\n--- Available Seats ---")
    available = [(i, j) for i in range(ROWS) for j in range(COLS) if seats[i][j] == 0]

    if available:
        for seat in available:
            print(f"Seat {seat} is available.")
    else:
        print("\nNo seats are available.")

def menu():
    while True:
        print("\n===== Cinema Seat Booking Menu =====")
        print("1. View Seat Layout")
        print("2. Book a Single Seat")
        print("3. Book Multiple Seats")
        print("4. Cancel a Seat Booking")
        print("5. Display Available Seats")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice (1 to 6): "))

            if choice == 1:
                viewSeats()
            elif choice == 2:
                bookSingleSeat()
            elif choice == 3:
                bookMultipleSeats()
            elif choice == 4:
                cancelSeat()
            elif choice == 5:
                displayAvailableSeats()
            elif choice == 6:
                print("\nExiting Seat Booking System... Thank You!\n")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 6.")
        except ValueError:
            print("\nPlease enter a valid number (1 to 6).")


if __name__ == "__main__":
    menu()