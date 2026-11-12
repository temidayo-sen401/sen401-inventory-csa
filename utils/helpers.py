"""Helper functions for analysing inventory items.

All functions are pure: they take a list of items and return a result
without changing the input or printing anything.
"""

from inventory import InventoryItem

DEFAULT_REORDER_THRESHOLD = 10


def item_value(item: InventoryItem) -> float:
    """Return the stock value of one item (quantity * price)."""
    return item["quantity"] * item["price"]


def total_stock_value(items: list[InventoryItem]) -> float:
    """Return the combined stock value of all items (0 for an empty list)."""
    return sum(item_value(item) for item in items)


def highest_stock_item(items: list[InventoryItem]) -> InventoryItem | None:
    """Return the item with the largest quantity, or None if ``items`` is empty."""
    if not items:
        return None
    return max(items, key=lambda item: item["quantity"])


def lowest_stock_item(items: list[InventoryItem]) -> InventoryItem | None:
    """Return the item with the smallest quantity, or None if ``items`` is empty."""
    if not items:
        return None
    return min(items, key=lambda item: item["quantity"])


def low_stock_items(
    items: list[InventoryItem], threshold: int = DEFAULT_REORDER_THRESHOLD
) -> list[InventoryItem]:
    """Return items whose quantity is below ``threshold`` and should be reordered."""
    return [item for item in items if item["quantity"] < threshold]
