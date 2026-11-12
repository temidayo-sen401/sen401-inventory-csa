"""Helper functions for the inventory."""


def highest_stock_item(items):
    if not items:  # Corrective fix: items[0] raised IndexError on empty list
        return None
    highest = items[0]
    for item in items:
        if item["quantity"] > highest["quantity"]:
            highest = item
    return highest


def lowest_stock_item(items):
    if not items:
        return None
    # Corrective fix: start from the first item, not 0. With 0 as the
    # starting value no quantity was ever lower, so this returned None.
    lowest = items[0]
    for item in items:
        if item["quantity"] < lowest["quantity"]:
            lowest = item
    return lowest
