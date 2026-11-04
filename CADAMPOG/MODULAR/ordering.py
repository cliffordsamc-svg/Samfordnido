def take_order(menu):
    orders = []

    while True:
        item_name = input("\nEnter menu item: ").strip().title()

        # allow "french fries" -> "French Fries" style matching
        match = None
        for name in menu:
            if name.lower() == item_name.lower():
                match = name

        if match:
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        break
                    print("Quantity must be at least 1.")
                except ValueError:
                    print("Please enter a valid number.")

            orders.append([match, quantity])
            print("Item added to your order.")
        else:
            print("Item not found in the menu.")

        another = input("Do you want to order another item? (yes/no): ")

        if another.strip().lower() == "no":
            break

    return orders