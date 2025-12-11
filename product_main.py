from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from  product_controller import ProductsController

def reset():
    product_name.set("")
    brand.set("")
    price.set(0)
    quantity.set(0)
    expire_date.set(str(datetime.now().date()))


    status, product_list = ProductsController.find_all()

    for item in table.get_children():
        table.delete(item)

    id_order = 0
    if status:
        for product in product_list:
            table.insert("", END, values=product)
            id_order = max(id_order, int(product[0]))
    else:
        messagebox.showerror("Error", product_list)
    p_id.set(id_order+1)


def select_product(event):
         product = table.item(table.focus())["values"]
         if product:
             p_id.set(product[0])
             product_name.set(product[1])
             brand.set(product[2])
             quantity.set(product[3])
             price.set(product[4])
             expire_date.set(product[5])

def save_click():
    status, message = ProductsController.save(
        p_id.get(),
        product_name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        expire_date.get(),

    )

    if status:
        reset()
        messagebox.showinfo("Save", message)
    else:
        messagebox.showerror("Error", message)

def edit_click():
    status, message = ProductsController.edit(
        p_id.get(),
        product_name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        expire_date.get()
    )

    if status:
        reset()
        messagebox.showinfo("Edit", message)
    else:
        messagebox.showerror("Error", message)

def remove_click():
    status, message = ProductsController.remove(p_id.get())


    if status:
        reset()
        messagebox.showinfo("remove", message)
    else:
        messagebox.showerror("Error", message)

window = Tk()
window.title("Super Market")
window.geometry("800x380")

# id
Label(window, text="Id").place(x=25, y=25)
p_id = IntVar()
Entry(window, textvariable=p_id,state="readonly").place(x=120, y=25)

# name
Label(window, text="Name").place(x=25, y=65)
product_name = StringVar()
Entry(window, textvariable=product_name).place(x=120, y=65)

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
Label(window, text="Expire Date").place(x=25, y=225)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=120, y=225)

Button(window, text="Save", width=18, command=save_click).place(x=50, y=330)
Button(window, text="Edit", width=18, command=edit_click).place(x=50, y=360)
Button(window, text="Remove", width=18, command=remove_click).place(x=50, y=390)

table = ttk.Treeview(window,columns=("ID","Name","Brand","Quantity","Price","Expire Date","Total"),show="headings")


table.column("ID", width=50)
table.column("Name", width=120)
table.column("Brand", width=120)
table.column("Quantity", width=100)
table.column("Expire Date", width=120)
table.column("Price", width=100)
table.column("Total", width=120)


table.heading("ID",text="ID")
table.heading("Name",text="Name")
table.heading("Brand",text="Brand")
table.heading("Quantity",text="Quantity")
table.heading("Price",text="Price")
table.heading("Expire Date",text="Expire Date")
table.heading("Total",text="Total")


table.place(x=300, y=25)
table.bind("<<TreeviewSelect>>", select_product)


reset()
window.mainloop()
