# app.py
from order_manager import OrderManager
from order import Order

def main():
    manager = OrderManager()

    # Add orders
    manager.add_order(Order(1, 'Alice', 'Apple', 10))
    manager.add_order(Order(2, 'Bob', 'Banana', 5))

    # View orders
    print(manager.view_order(1))
    print(manager.view_order(2))

    # Update an order
    manager.update_order(1, quantity=15)
    print(manager.view_order(1))

if __name__ == '__main__':
    main()
