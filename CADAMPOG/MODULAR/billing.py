def calculate_order(menu, orders):
    total = 0
    receipt = []

    for order in orders:
        item_name = order[0]
        quantity = order[1]
        price = menu[item_name]
        item_total = price * quantity

        receipt.append([item_name, quantity, price, item_total])
        total += item_total

    return receipt, total