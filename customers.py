import json
def read_orders(filename):
        with open(filename, 'r') as f:
            return json.load(f)

def extract_customer_data(orders):
    customer_data = {}
    for order in orders:
        name = order.get("name")
        phone = order.get("phone")
        if name and phone:
            customer_data[name] = phone
    return customer_data

def main():
    orders = read_orders('example_orders.json')
    customer_data = extract_customer_data(orders)
    with open('customers.json', 'w') as f:
        json.dump(customer_data, f) 

if __name__ == "__main__":
    main()
