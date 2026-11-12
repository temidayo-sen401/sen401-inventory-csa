"""Helper functions for the inventory."""

from inventory import InventoryItem


def highest_stock_item(items: list[InventoryItem]) -> InventoryItem | None:
    if not items:  # Corrective fix: items[0] raised IndexError on empty list
        return None
    highest = items[0]
    for item in items:
        if item["quantity"] > highest["quantity"]:
            highest = item
    return highest


def lowest_stock_item(items: list[InventoryItem]) -> InventoryItem | None:
    if not items:
        return None
    # Corrective fix: start from the first item, not 0. With 0 as the
    # starting value no quantity was ever lower, so this returned None.
    lowest = items[0]
    for item in items:
        if item["quantity"] < lowest["quantity"]:
            lowest = item
    return lowest


def item_value(item: InventoryItem) -> float:
    """Perfective: stock value of a single item (quantity * price)."""
    return item["quantity"] * item["price"]


def low_stock_items(items: list[InventoryItem], threshold: int = 10) -> list[InventoryItem]:
    """Perfective: return items whose quantity is below the reorder threshold."""
    return [item for item in items if item["quantity"] < threshold]
