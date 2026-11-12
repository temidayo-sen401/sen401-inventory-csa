"""Inventory app: prints a stock report and exports the inventory to CSV.

Run with:  python3.12 app.py
"""

from inventory import InventoryItem, export_to_csv, inventory
from utils.helpers import (
    highest_stock_item,
    item_value,
    low_stock_items,
    lowest_stock_item,
    total_stock_value,
)

WIDTH = 62
LINE = "=" * WIDTH
RULE = "-" * WIDTH


def print_stock_table(items: list[InventoryItem]) -> None:
    """Print each item with its quantity, unit price and stock value, then the total."""
    print(f"{'Item':<18}{'Qty':>6}{'Unit Price (N)':>17}{'Value (N)':>21}")
    print(RULE)
    for item in items:
        print(
            f"{item['item_name']:<18}{item['quantity']:>6}"
            f"{item['price']:>17,.2f}{item_value(item):>21,.2f}"
        )
    print(RULE)
    print(f"{'TOTAL STOCK VALUE':<41}{total_stock_value(items):>21,.2f}")


def print_stock_levels(items: list[InventoryItem]) -> None:
    """Print the highest and lowest stocked items and any low-stock alerts."""
    highest = highest_stock_item(items)
    lowest = lowest_stock_item(items)
    if highest and lowest:
        print(f"Highest stock item : {highest['item_name']} ({highest['quantity']} units)")
        print(f"Lowest stock item  : {lowest['item_name']} ({lowest['quantity']} units)")
    for item in low_stock_items(items):
        print(f"LOW STOCK ALERT    : {item['item_name']} has only {item['quantity']} left - reorder")


def main() -> None:
    """Run the inventory report."""
    print(LINE)
    print("INVENTORY STOCK REPORT".center(WIDTH))
    print(LINE)
    print_stock_table(inventory)
    print(LINE)
    print_stock_levels(inventory)
    print(f"Exported inventory : {export_to_csv(inventory)}")


if __name__ == "__main__":
    main()
