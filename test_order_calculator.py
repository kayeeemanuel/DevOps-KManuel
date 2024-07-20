# test_order_calculator.py
import unittest
from order_calculator import calculate_total_charges

class TestOrderCalculator(unittest.TestCase):

    def test_dine_in(self):
        self.assertEqual(calculate_total_charges(100, 1), 108.00)

    def test_pick_up(self):
        self.assertEqual(calculate_total_charges(100, 2), 100.00)

    def test_delivery(self):
        self.assertEqual(calculate_total_charges(100, 3), 110.00)

    def test_invalid_order_type(self):
        with self.assertRaises(ValueError):
            calculate_total_charges(100, 4)

    def test_negative_cost(self):
        with self.assertRaises(ValueError):
            calculate_total_charges(-100, 1)

if __name__ == '__main__':
    unittest.main()
