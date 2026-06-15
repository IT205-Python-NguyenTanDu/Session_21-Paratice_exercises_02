import unittest
from feature_2 import process_add_to_order
from feature_3 import calculate_total


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}


class TestHighlandsPOS(unittest.TestCase):
    """Unit tests for Highlands Mini POS."""

    def test_calculate_total(self):
        """Total price should be calculated correctly."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {"code": "F1", "name": "Freeze Trà Xanh", "price": 55000, "quantity": 1}
        ]
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Negative quantity should raise ValueError."""
        with self.assertRaises(ValueError):
            process_add_to_order(DRINK_MENU, [], "P1", -1)

    def test_invalid_quantity_zero(self):
        """Zero quantity should raise ValueError."""
        with self.assertRaises(ValueError):
            process_add_to_order(DRINK_MENU, [], "P1", 0)

    def test_item_not_found(self):
        """Invalid drink code should raise Exception."""
        with self.assertRaises(Exception):
            process_add_to_order(DRINK_MENU, [], "A1", 2)

    def test_add_to_order_success(self):
        """Valid order should be added to current_order correctly."""
        order = process_add_to_order(DRINK_MENU, [], "P1", 2)
        self.assertEqual(len(order), 1)
        self.assertEqual(order[0]["quantity"], 2)
        self.assertEqual(order[0]["price"], 35000)

    def test_calculate_total_empty(self):
        """Empty order should return total of zero."""
        result = calculate_total([])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
