# order_manager.py
from order import Order

class OrderManager:
    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        self.orders[order.order_id] = order

    def view_order(self, order_id):
        return self.orders.get(order_id, None)

    def update_order(self, order_id, customer_name=None, item=None, quantity=None):
        order = self.orders.get(order_id, None)
        if order:
            if customer_name:
                order.customer_name = customer_name
            if item:
                order.item = item
            if quantity:
                order.quantity = quantity
            return order
        return None
