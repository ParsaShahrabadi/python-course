import re
from datetime import datetime,date,time
from sys import exec_prefix
from tkinter import messagebox
product_list=[]


def save(name,brand,price,quantity,expire_date):
    try:
        name_validator(name.get())
        brand_validator(brand.get())
        price_validator(price.get())
        quantity_validator(quantity.get())
        expire_date_validator(expire_date.get())

        product = {"name":name.get(),
                   "brand":brand.get(),
                   "price":price.get(),
                   "quantity":quantity.get(),
                   "expire_date":expire_date.get()}
        product_list.append(product)

        messagebox.showinfo("Success","Product has been saved")
        name.set("")
        brand.set("")
        price.set(0)
        quantity.set(0)
        expire_date.set(0)
    except Exception as e:
        messagebox.showerror("Save Error",f"Error : {e}")


def name_validator(name):
    if not re.match("^[a-zA-Z\s]{3,30}$",name):
        raise ValueError("Invalid name")

def brand_validator(brand):
    if not re.match("^[a-zA-Z\s]{3,30}$",brand):
        raise ValueError("Invalid brand")

def price_validator(price):
    if not price > 0:
        raise ValueError("Invalid price")

def quantity_validator(quantity):
    if not quantity > 0:
        raise ValueError("Invalid quantity")

def expire_date_validator(expire_date):
    if not datetime.strptime(expire_date,'%Y-%m-%d').date() > date.today():
        raise ValueError("Invalid expire")






