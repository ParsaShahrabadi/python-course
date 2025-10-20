import re
from datetime import datetime,date,time
from tkinter import *
from tkinter import *


# product_list = []
# def data_validation(name, brand, quantity, price, expire_date):
#     if re.match(r"^[a-zA-Z\s]{3,30}$", name) and re.match(r"^[a-zA-Z\s]{3,30}$",brand) and quantity>0 and price>0 and expire_date > date.today():
#         return True
#     else:
#         print("data invalid")

# def get_data():
#     name = input("Enter your name: ")
#     brand = (input("Enter your brand: "))
#     quantity = int(input("Enter your quantity: "))
#     price = int(input("Enter your price: "))
#     expire_date = datetime.strptime(input("Enter your expire date(YYYY-MM-DD)"), '%Y-%m-%d').date()
#
#     if data_validation(name, brand, quantity, price, expire_date):
#         product = {"name":name,"brand":brand,"quantity":quantity,"price":price,"expire_date":expire_date}
#         return product
#     else:
#         return None

# def show_product(product_list):
#     for product in product_list:
#         sum_product = product["quantity"] * product["price"]
#         print(f"{product['name']:<10} {product['brand']:<8} {product['quantity']:>4} {product['price']:>8}")
#     print("---------------------------------------")
#     print("sum: ",sum_product)

def save():



window = Tk()
window.title("Super Market")
window.geometry("500x400")


#name
Label(window, text="name").place(x = 25, y = 25)
name = StringVar()
Entry(window, textvariable=name).place(x = 100,y = 25)

#brand
Label(window, text="brand").place(x = 25, y = 50)
brand = StringVar()
Entry(window, textvariable=brand).place(x = 100,y = 50)

#quantity
Label(window, text="brand" ).place(x = 25,y = 75)
brand= IntVar()
Entry(window,textvariable=brand).place(x = 100,y = 75)

#price
Label(window, text="price").place(x = 25,y = 100)
price = IntVar()
Entry(window, textvariable=price).place(x =100,y = 100)

# expier_date
Label(window,text="expire_date").place(x = 25,y = 125)
expire_date = StringVar()
Entry(window,textvariable=expire_date).place(x = 100,y = 125)








window.mainloop()




