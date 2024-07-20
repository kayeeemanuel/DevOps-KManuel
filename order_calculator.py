# order_calculator.py

def calculate_total_charges(order_cost, order_type):
    if order_type == 1:  # dine-in
        service_charge = order_cost * 0.08
        total_amount = order_cost + service_charge
    elif order_type == 2:  # pick-up
        total_amount = order_cost
    elif order_type == 3:  # delivery
        service_charge = order_cost * 0.10
        total_amount = order_cost + service_charge
    else:  # invalid order type
        raise ValueError("Invalid order type.")

    return round(total_amount, 2)

if __name__ == "__main__":
    order_cost = float(input("Please enter the order cost in AUD: "))
    order_type = int(input("Please enter the order type (1 for dine-in, 2 for pick-up or 3 for delivery): "))
    
    try:
        total_amount = calculate_total_charges(order_cost, order_type)
        print("Total amount to be paid: $", total_amount)
    except ValueError as e:
        print(e)
