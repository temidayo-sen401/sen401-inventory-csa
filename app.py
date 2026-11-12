"""Inventory app: calculates the total stock value."""

from inventory import export_to_csv, inventory
from utils.helpers import highest_stock_item, item_value, low_stock_items, lowest_stock_item

LINE = "=" * 62

print(LINE)
print("INVENTORY STOCK REPORT".center(62))
print(LINE)

# Perfective: formatted table with per-item stock value
print(f"{'Item':<18}{'Qty':>6}{'Unit Price (N)':>17}{'Value (N)':>21}")
print("-" * 62)
total = 0
for item in inventory:
    # Corrective fix: stock value is quantity * price (was quantity + price)
    value = item_value(item)
    total += value
    print(f"{item['item_name']:<18}{item['quantity']:>6}{item['price']:>17,.2f}{value:>21,.2f}")
print("-" * 62)
print(f"{'TOTAL STOCK VALUE':<41}{total:>21,.2f}")
print(LINE)

highest = highest_stock_item(inventory)
lowest = lowest_stock_item(inventory)
print(f"Highest stock item : {highest['item_name']} ({highest['quantity']} units)")
print(f"Lowest stock item  : {lowest['item_name']} ({lowest['quantity']} units)")

# Perfective: low-stock alert
for item in low_stock_items(inventory):
    print(f"LOW STOCK ALERT    : {item['item_name']} has only {item['quantity']} left - reorder")

# Adaptive (new feature): export the inventory to CSV
print(f"Exported inventory : {export_to_csv(inventory)}")
