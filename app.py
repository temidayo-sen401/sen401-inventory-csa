"""Inventory app: calculates the total stock value."""

from inventory import inventory
from utils.helpers import highest_stock_item, lowest_stock_item

total = 0
for item in inventory:
    total += item["quantity"] + item["price"]

print("Total stock value:", total)
print("Highest stock item:", highest_stock_item(inventory))
print("Lowest stock item:", lowest_stock_item(inventory))
