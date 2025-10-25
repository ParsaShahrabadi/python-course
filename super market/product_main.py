from tkinter import *
from product_module import *
from datetime import date


def total():
    total_price = 0
    for product in product_list:
        total_price += product["quantity"] * product["price"]
    messagebox.showinfo("Success", f"Total : {total_price}")


def save():
    try:
        name_validator(name.get())
        brand_validator(brand.get())
        price_validator(price.get())
        quantity_validator(quantity.get())
        expire_date_validator(expire_date.get())

        product = {
            "id": id.get(),
            "name": name.get(),
            "brand": brand.get(),
            "price": price.get(),
            "quantity": quantity.get(),
            "expire_date": expire_date.get()
        }
        product_list.append(product)

        messagebox.showinfo("Success", "Product has been saved")
        id.set(0)
        name.set("")
        brand.set("")
        price.set(0)
        quantity.set(0)
        expire_date.set(str(date.today()))
    except Exception as e:
        messagebox.showerror("Save Error", f"Error : {e}")


window = Tk()
window.title("Super Market")
window.geometry("300x420")

# id
Label(window, text="Id").place(x=25, y=25)
id = IntVar()
Entry(window, textvariable=id).place(x=100, y=25)

# name
Label(window, text="Name").place(x=25, y=65)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=65)

# brand
Label(window, text="Brand").place(x=25, y=105)
brand = StringVar()
Entry(window, textvariable=brand).place(x=100, y=105)

# quantity
Label(window, text="Quantity").place(x=25, y=145)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=100, y=145)

# price
Label(window, text="Price").place(x=25, y=185)
price = IntVar()
Entry(window, textvariable=price).place(x=100, y=185)

# expire_date
Label(window, text="Expire Date").place(x=25, y=225)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=100, y=225)

Button(window, text="Save", command=save).place(x=100, y=300, width=80)
Button(window, text="Total", command=total).place(x=100, y=350, width=80)

window.mainloop()
