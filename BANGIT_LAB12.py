def display_menu():
    """Displays the food menu with prices."""
    menu = {
        1: ("Burger", 5.99),
        2: ("Pizza", 8.99),
        3: ("Sandwich", 4.99),
        4: ("Pasta", 7.49),
        5: ("Salad", 6.49),
    }
    print("\n--- Menu ---")
    for key, (item, price) in menu.items():
        print(f"{key}. {item} - ${price:.2f}")
    return menu

def select_item(menu):
    """Allows the user to select an item from the menu."""
    while True:
        try:
            choice = int(input("\nEnter the number of the item you'd like to order: "))
            if choice in menu:
                item, price = menu[choice]
                print(f"You selected: {item} - ${price:.2f}")
                return price
            else:
                print("Invalid choice. Please select a valid menu item.")
        except ValueError:
            print("Please enter a number.")

def process_payment(total):
    """Handles payment and validates if sufficient cash is provided."""
    while True:
        try:
            cash = float(input(f"\nYour total is ${total:.2f}. Enter cash amount: $"))
            if cash >= total:
                change = cash - total
                print(f"Payment accepted. Your change is ${change:.2f}.")
                break
            else:
                print(f"Insufficient cash. You need at least ${total:.2f}.")
        except ValueError:
            print("Please enter a valid amount.")

def main():
    """Main function to run the food ordering system."""
    menu = display_menu()
    total = select_item(menu)
    process_payment(total)

if __name__ == "__main__":
    main()
