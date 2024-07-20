# test_order_manager.py
import unittest
from order_manager import OrderManager
from order import Order

class TestOrderManager(unittest.TestCase):

    def setUp(self):
        self.manager = OrderManager()
        self.order1 = Order(1, 'Alice', 'Apple', 10)
        self.order2 = Order(2, 'Bob', 'Banana', 5)
        self.manager.add_order(self.order1)
        self.manager.add_order(self.order2)

    def test_add_order(self):
        self.assertIn(1, self.manager.orders)
        self.assertIn(2, self.manager.orders)

    def test_view_order(self):
        order = self.manager.view_order(1)
        self.assertEqual(order.customer_name, 'Alice')
        self.assertEqual(order.item, 'Apple')
        self.assertEqual(order.quantity, 10)

    def test_update_order(self):
        self.manager.update_order(1, quantity=15)
        order = self.manager.view_order(1)
        self.assertEqual(order.quantity, 15)

    def test_view_nonexistent_order(self):
        order = self.manager.view_order(3)
        self.assertIsNone(order)

    def test_update_nonexistent_order(self):
        result = self.manager.update_order(3, quantity=20)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
