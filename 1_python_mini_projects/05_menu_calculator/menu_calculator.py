def display_menu():
    """Display the calculator menu options."""
    print("=" * 25)
    print("== Menu Calculator ==")
    print("=" * 25)
    print("Please Choose Your Operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()
    
def get_input(p):
    """
    Prompt the user for a number input.
    Repeats until a valid float is entered.
    """
    while True:
        try:
            return float(input(p))
        except ValueError:
            print("Invalid input! Please enter a number.")

def perform_calculation(choice, num1, num2):
    """
    Perform the selected arithmetic operation.
    Returns the result or None if division by zero occurs.
    """
    match choice:
        case 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case 3:
            result = num1 * num2
            print(f"{num1} × {num2} = {result}")
        case 4:
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return None
            result = num1 / num2
            print(f"{num1} ÷ {num2} = {result}")
    return result

def main():
    """Main calculator loop: handles menu, input, and calculation."""
    while True:   
        display_menu()
        
        # Get and validate menu choice
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1-5.")
            continue  # Prompt again if input is invalid
        
        # Handle exit and invalid choices
        if choice == 5:
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select between 1-5.")
            continue

        # Get two numbers from the user
        num1 = get_input("Enter the first number: ")
        num2 = get_input("Enter the second number: ")
        
        # Perform calculation and display result
        result = perform_calculation(choice, num1, num2)
        if result is not None:
            print(f"Stored result: {result}")

if __name__ == "__main__":
    main()
