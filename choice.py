import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For other platforms

def print_menu():
    clear_screen()

    menu = [
        "1. Get the statistical analysis of Age vs Deaths",
        "2. Get the statistical analysis of Ethnicity vs Deaths",
        "3. Get the statistical analysis of Medical_condition vs Deaths",
        "4. Get the statistical analysis of ICU_type vs Deaths",
        "5. Get the statistical analysis of BMI vs Deaths",
        "0. Exit"
    ]

    # Default terminal size if obtaining size fails
    try:
        terminal_size = os.get_terminal_size()
        lines = terminal_size.lines
    except OSError:
        lines = 25  # Default to 25 lines if terminal size cannot be obtained

    # Print menu with appropriate spacing
    print("\n" * (lines // 3))
    print("CHOICE MENU")
    print("-" * terminal_size.columns)

    for line in menu:
        print(line)

    print("-" * terminal_size.columns)

def show_menu():
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice (0-5): "))
            if choice == 0:
                clear_screen()
                print("Goodbye!")
                break
            elif choice in [1, 2, 3, 4, 5]:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return choice