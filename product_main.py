
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime, date, time
from  product_controller import ProductsController




def reset_form():
    id.set(0)
    name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)
    expire_date.set(str(date.today()))
    total.set("")
    status, product_list = ProductsController.find_all()

    for item in table.get_children():
        table.delete(item)

    for person in product_list:
        table.insert("", END, values=person)

def select_product(event):
         product = table.item(table.focus())["values"]

window = Tk()
window.title("Super Market")
window.geometry("800x380")

# id
Label(window, text="Id").place(x=25, y=25)
user_id = IntVar()
Entry(window, textvariable=user_id,state="readonly").place(x=120, y=25)

# name
Label(window, text="Name").place(x=25, y=65)
name = StringVar()
Entry(window, textvariable=name).place(x=120, y=65)

# brand
Label(window, text="Brand").place(x=25, y=105)
brand = StringVar()
Entry(window, textvariable=brand).place(x=120, y=105)

# quantity
Label(window, text="Quantity").place(x=25, y=145)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=120, y=145)

# price
Label(window, text="Price").place(x=25, y=185)
price = IntVar()
Entry(window, textvariable=price).place(x=120, y=185)

# expire_date
Label(window, text="Expiration Date\nYYYY-MM-DD").place(x=25, y=225)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=120, y=225)

Button(window, text="Add", command=add).place(x=145, y=280, width=100)
Button(window, text="Total", command=total).place(x=25, y=280, width=100)

table = ttk.Treeview(window,columns=(1,2,3,4,5,6),height=15,show="headings")
table.heading(1,text="ID")
table.heading(2,text="Name")
table.heading(3,text="Brand")
table.heading(4,text="Quantity")
table.heading(5,text="Price")
table.heading(6,text="Expire Date")

table.column(1,width=50)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=60)
table.column(5,width=60)
table.column(6,width=100)

table.place(x=300, y=25)



reset_form()
window.mainloop()
