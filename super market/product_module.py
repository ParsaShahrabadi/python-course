import re
from datetime import datetime, date, time
from sys import exec_prefix
from tkinter import messagebox

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



