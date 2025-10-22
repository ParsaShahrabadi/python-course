from tkinter import *
from product_module import *

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
Label(window, text="quantity" ).place(x = 25,y = 75)
quantity= IntVar()
Entry(window,textvariable=quantity).place(x = 100,y = 75)

#price
Label(window, text="price").place(x = 25,y = 100)
price = IntVar()
Entry(window, textvariable=price).place(x =100,y = 100)

# expier_date
Label(window,text="expire_date").place(x = 25,y = 125)
expire_date = StringVar()
Entry(window,textvariable=expire_date).place(x = 100,y = 125)

Button(window,text="save", command = lambda:save(name,brand,price,quantity,expire_date)).place(x = 100,y = 150, width = 125)
Button(window,text="Total",command = lambda:total(quantity,price) ).place(x = 100,y = 175, width = 125)


window.mainloop()











