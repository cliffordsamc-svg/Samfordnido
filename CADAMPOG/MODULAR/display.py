from menu import get_menu
from display import display_menu, print_receipt
from ordering import take_order
from billing import calculate_order


def main():
    menu = get_menu()

    display_menu(menu)

    want_order = input("\nDo you want to order? (yes/no): ")

    if want_order.strip().lower() == "yes":
        orders = take_order(menu)

        if len(orders) > 0:
            receipt, total = calculate_order(menu, orders)
            print_receipt(receipt, total)
        else:
            print("No order was made.")
    else:
        print("Thank you! Goodbye.")


main()