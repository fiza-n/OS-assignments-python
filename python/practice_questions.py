products = [
    {"name": "Laptop", "price": 999.99, "quantity": 5},
    {"name": "Mouse", "price": 25.50, "quantity": 20},
    {"name": "Keyboard", "price": 45.00, "quantity": 0},
    {"name": "Monitor", "price": 199.99, "quantity": 8},
]

# print(type(products[0]['price']))


def inventory_report(products):
    grand_total = 0
    for index,keys in enumerate(products, start=1):
        total = 0
        if(keys['quantity'] == 0):
               print(f"{keys['name']} is out of stock")
               continue
        total = keys['price'] * keys['quantity']
        grand_total +=total
        print(f"{keys['name']}: ${total:.2f}")
    print(f'Inventory total value is : ${grand_total:.2f}')
   

inventory_report(products)