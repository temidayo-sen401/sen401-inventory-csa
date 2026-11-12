"""Inventory app: calculates the total stock value."""

from inventory import export_to_csv, inventory
from utils.helpers import highest_stock_item, lowest_stock_item

total = 0
for item in inventory:
    # Corrective fix: stock value is quantity * price (was quantity + price)
    total += item["quantity"] * item["price"]

print("Total stock value:", total)
print("Highest stock item:", highest_stock_item(inventory))
print("Lowest stock item:", lowest_stock_item(inventory))

# Adaptive (new feature): export the inventory to CSV
print("Exported inventory to:", export_to_csv(inventory))
