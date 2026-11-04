class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []  # list of [MenuItem, quantity]

    def add_item(self, menu_item, quantity):
        self.items.append([menu_item, quantity])

    def is_empty(self):
        return len(self.items) == 0

    def get_total(self):
        total = 0
        for menu_item, quantity in self.items:
            total += menu_item.price * quantity
        return total


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.load_menu()

    def load_menu(self):
        self.add_menu_item("Burger", 80)
        self.add_menu_item("Chicken", 120)
        self.add_menu_item("Spaghetti", 100)
        self.add_menu_item("French Fries", 60)
        self.add_menu_item("Softdrink", 40)

    def add_menu_item(self, name, price):
        self.menu[name.lower()] = MenuItem(name, price)

    def display_menu(self):
        print("\n===== FAST FOOD MENU =====")

        number = 1
        for item in self.menu.values():
            print(number, ".", item.name, "- P", item.price)
            number += 1

    def ask_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    return quantity
                print("Quantity must be at least 1.")
            except ValueError:
                print("Please enter a valid number.")

    def take_order(self):
        order = Order()

        while True:
            item_name = input("\nEnter menu item: ").strip().lower()

            if item_name in self.menu:
                quantity = self.ask_quantity()
                order.add_item(self.menu[item_name], quantity)
                print("Item added to your order.")
            else:
                print("Item not found in the menu.")

            another = input("Do you want to order another item? (yes/no): ")

            if another.strip().lower() == "no":
                break

        return order

    def print_receipt(self, order):
        print("\n========== RECEIPT ==========")
        print("Item\t\tQty\tPrice\tTotal")

        for menu_item, quantity in order.items:
            item_total = menu_item.price * quantity
            print(menu_item.name, "\t\t", quantity, "\tP", menu_item.price, "\tP", item_total)

        print("-----------------------------")
        print("TOTAL: P", order.get_total())
        print("=============================")

    def run(self):
        self.display_menu()

        want_order = input("\nDo you want to order? (yes/no): ")

        if want_order.strip().lower() == "yes":
            order = self.take_order()

            if not order.is_empty():
                self.print_receipt(order)
            else:
                print("No order was made.")
        else:
            print("Thank you! Goodbye.")