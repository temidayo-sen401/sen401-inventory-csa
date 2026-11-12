"""Unit tests for utils.helpers (standard-library unittest, no extra dependencies).

Run with:  python3.12 -m unittest -v
"""

import unittest

from utils.helpers import (
    highest_stock_item,
    item_value,
    low_stock_items,
    lowest_stock_item,
    total_stock_value,
)

SAMPLE = [
    {"item_name": "A", "quantity": 2, "price": 100.0},
    {"item_name": "B", "quantity": 50, "price": 10.0},
    {"item_name": "C", "quantity": 8, "price": 25.0},
]


class HelperTests(unittest.TestCase):
    def test_item_value(self):
        self.assertEqual(item_value(SAMPLE[0]), 200.0)

    def test_total_stock_value(self):
        # Regression test for the quantity + price bug
        self.assertEqual(total_stock_value(SAMPLE), 200 + 500 + 200)

    def test_highest_and_lowest(self):
        self.assertEqual(highest_stock_item(SAMPLE)["item_name"], "B")
        self.assertEqual(lowest_stock_item(SAMPLE)["item_name"], "A")

    def test_empty_list(self):
        self.assertIsNone(highest_stock_item([]))
        self.assertIsNone(lowest_stock_item([]))
        self.assertEqual(total_stock_value([]), 0)

    def test_low_stock_items(self):
        names = [i["item_name"] for i in low_stock_items(SAMPLE)]
        self.assertEqual(names, ["A", "C"])


if __name__ == "__main__":
    unittest.main()
