"""Helper functions for the inventory."""


def highest_stock_item(items):
    highest = items[0]
    for item in items:
        if item["quantity"] > highest["quantity"]:
            highest = item
    return highest


def lowest_stock_item(items):
    lowest = None
    lowest_qty = 0
    for item in items:
        if item["quantity"] < lowest_qty:
            lowest = item
            lowest_qty = item["quantity"]
    return lowest
