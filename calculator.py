"""Interactive calculator and unit converter."""


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def run_calculator():
    while True:
        print("\nCalculator")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Return to main menu")

        choice = input("Choose an operation: ").strip()

        if choice == "5":
            return
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please choose 1 through 5.")
            continue

        first = get_number("Enter the first number: ")
        second = get_number("Enter the second number: ")

        if choice == "1":
            result = first + second
        elif choice == "2":
            result = first - second
        elif choice == "3":
            result = first * second
        else:
            if second == 0:
                print("Cannot divide by zero.")
                continue
            result = first / second

        print(f"Result: {result:g}")


def run_converter():
    while True:
        print("\nUnit Converter")
        print("1. Kilometers to miles")
        print("2. Celsius to Fahrenheit")
        print("3. Return to main menu")

        choice = input("Choose a conversion: ").strip()

        if choice == "3":
            return
        if choice not in {"1", "2"}:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        value = get_number("Enter the value to convert: ")

        if choice == "1":
            converted = value * 0.621371
            print(f"{value:g} km = {converted:.4f} miles")
        else:
            converted = (value * 9 / 5) + 32
            print(f"{value:g}°C = {converted:.2f}°F")


def main():
    while True:
        print("\nCalculator and Unit Converter")
        print("1. Calculator")
        print("2. Unit converter")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_calculator()
        elif choice == "2":
            run_converter()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
