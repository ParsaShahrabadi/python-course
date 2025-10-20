import re
from datetime import datetime,date,time
from functools import total_ordering

total = 0
product_list = []
def data_validation(name, brand, quantity, price, expire_date):
    if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$",brand) and quantity>0 and price>0 and expire_date > date.today():
        return True
    else:
        print("data invalid")

def get_data():
    name = input("Enter your name: ")
    brand = (input("Enter your brand: "))
    quantity = int(input("Enter your quantity: "))
    price = int(input("Enter your price: "))
    expire_date = datetime.strptime(input("Enter your expire date(YYYY-MM-DD)"), '%Y-%m-%d').date()

    if data_validation(name, brand, quantity, price, expire_date):
        product = {"name":name,"brand":brand,"quantity":quantity,"price":price,"expire_date":expire_date}
        return product
    else:
        return None

def show_product(product_list):
    for product in product_list:
        sum_product = product["quantity"] * product["price"]
        print(f"{product['name']:<10} {product['brand']:<8} {product['quantity']:>4} {product['price']:>8}")
    print("---------------------------------------")
    print("sum: ",sum_product)


