celToFah = 9.0 / 5.0
fahToCel = 5.0 / 9.0
fahOffset = 32
kelvinOffset = 273.15

def celsiusToFahrenheit():
    temp = float(input("Enter temperature in celsius: "))
    converted = (temp * celToFah) + fahOffset
    print(f"{temp} C = {converted} F")

def celsiusToKelvin():
    temp = float(input("Enter temperature in celsius: "))
    converted = temp + kelvinOffset
    print(f"{temp} C = {converted} K")

def fahrenheitToCelsius():
    temp = float(input("Enter temperature in fahrenheit: "))
    converted = (temp - fahOffset) * fahToCel
    print(f"{temp} F = {converted} C")

def fahrenheitToKelvin():
    temp = float(input("Enter temperature in fahrenheit: "))
    converted = (temp - fahOffset) * fahToCel + kelvinOffset
    print(f"{temp} F = {converted} K")

def kelvinToCelsius():
    temp = float(input("Enter temperature in kelvin: "))
    converted = temp - kelvinOffset
    print(f"{temp} K = {converted} C")

def kelvinToFahrenheit():
    temp = float(input("Enter temperature in kelvin: "))
    converted = ((temp - kelvinOffset) * celToFah) + fahOffset
    print(f"{temp} K = {converted} F")

def exit_program():
    print("\nExiting Temperature Converter...\n")

if __name__ == "__main__":
    while True:
        print("\n---Temperature Converter---\n")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit\n")

        choice = int(input("Enter your choice(1-7): "))

        if choice == 7:
            exit_program()
            break

        elif choice == 1:
            celsiusToFahrenheit()

        elif choice == 2:
            celsiusToKelvin()

        elif choice == 3:
            fahrenheitToCelsius()

        elif choice == 4:
            fahrenheitToKelvin()

        elif choice == 5:
            kelvinToCelsius()

        elif choice == 6:
            kelvinToFahrenheit()

        else:
            print("Invalid choice. Try again.")