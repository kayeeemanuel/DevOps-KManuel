# order.py
class Order:
    def __init__(self, order_id, customer_name, item, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity

    def __str__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self.item}, {self.quantity})"
