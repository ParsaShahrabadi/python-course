import re
from datetime import datetime, date, time


product_list = []


def name_validator(name):
    if not re.match("^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid name")


def brand_validator(brand):
    if not re.match("^[a-zA-Z\s]{3,30}$", brand):
        raise ValueError("Invalid brand")


def price_validator(price):
    if not price > 0:
        raise ValueError("Invalid price")


def quantity_validator(quantity):
    if not quantity > 0:
        raise ValueError("Invalid quantity")


def expire_date_validator(expire_date):
    if not datetime.strptime(expire_date, '%Y-%m-%d').date() > date.today():
        raise ValueError("Invalid expire")

def create_product_and_validat(user_id,name,brand,quantity,price,expire_date):
    name_validator(name)
    brand_validator(brand)
    price_validator(price)
    quantity_validator(quantity)
    expire_date_validator(expire_date)

    product = {
        "id": user_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity,
        "expire_date": expire_date
    }
    return product

def calculate_total(product_list):
    if not product_list:
        raise ValueError("no product","no product available")
    total_price = 0
    for product in product_list:
        total_price += product["quantity"] * product["price"]
    return total_price


print(product_list)