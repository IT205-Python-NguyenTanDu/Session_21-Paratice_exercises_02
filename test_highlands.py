import unittest

from feature_2 import process_add_to_order
from feature_3 import calculate_total
from exceptions import InvalidQuantityError, ItemNotFoundError


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}


class TestHighlandsPOS(unittest.TestCase):
    """Unit tests for Highlands Mini POS."""

    def test_calculate_total(self):
        """Total price should be calculated correctly across multiple items."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1},
        ]
        self.assertEqual(calculate_total(mock_order), 125000)

    def test_calculate_total_empty(self):
        """Empty order should return total of zero."""
        self.assertEqual(calculate_total([]), 0)

    def test_add_to_order_success(self):
        """Valid code and quantity should append the item to the order."""
        order = process_add_to_order(DRINK_MENU, [], "P1", 2)
        self.assertEqual(len(order), 1)
        self.assertEqual(order[0]["quantity"], 2)
        self.assertEqual(order[0]["price"], 35000)

    def test_invalid_quantity_negative(self):
        """Negative quantity should raise InvalidQuantityError."""
        with self.assertRaises(InvalidQuantityError):
            process_add_to_order(DRINK_MENU, [], "P1", -1)

    def test_invalid_quantity_zero(self):
        """Zero quantity should raise InvalidQuantityError."""
        with self.assertRaises(InvalidQuantityError):
            process_add_to_order(DRINK_MENU, [], "P1", 0)

    def test_item_not_found(self):
        """Unknown drink code should raise ItemNotFoundError."""
        with self.assertRaises(ItemNotFoundError):
            process_add_to_order(DRINK_MENU, [], "A1", 2)


if __name__ == "__main__":
    unittest.main()
