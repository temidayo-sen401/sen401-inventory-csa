"""Inventory data module: list of items in stock.

Requires Python 3.12+ (uses the PEP 695 ``type`` statement).
"""

import csv
from pathlib import Path

# Adaptive: Python 3.12 type alias syntax (PEP 695)
type InventoryItem = dict[str, str | int | float]

inventory: list[InventoryItem] = [
    {"item_name": "Laptop", "quantity": 12, "price": 450000.00},
    {"item_name": "Mouse", "quantity": 85, "price": 7500.00},
    {"item_name": "Keyboard", "quantity": 40, "price": 15000.00},
    {"item_name": "Monitor", "quantity": 18, "price": 120000.00},
    {"item_name": "USB Flash Drive", "quantity": 150, "price": 4500.00},
    {"item_name": "Printer", "quantity": 5, "price": 210000.00},
]


def export_to_csv(items: list[InventoryItem], path: str | Path = "inventory.csv") -> Path:
    """Adaptive (new feature): write the inventory to a CSV file using the csv module."""
    path = Path(path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["item_name", "quantity", "price"])
        writer.writeheader()
        writer.writerows(items)
    return path
