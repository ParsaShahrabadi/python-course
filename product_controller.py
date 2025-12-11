import re
from datetime import datetime
from product_modell import Product
from product_dao import ProductsDataAccecc


class ProductsController:
    @staticmethod


    #validating products information


    def validator(product_name, brand, quantity, price, expire_date,):

        if not re.match(r"^[a-zA-Z\s]{3,30}$", product_name):
            raise ValueError("Invalid name")

        if not re.match(r"^[a-zA-Z0-9\s]{3,30}$", brand):
            raise ValueError("Invalid brand")

        if not int(price) > 0:
            raise ValueError("Invalid price")

        if not int(quantity) > 0:
            raise ValueError("Invalid quantity")


        try:
            datetime.strptime(expire_date, "%Y-%m-%d")
        except ValueError:
            raise NameError("Invalid EXPIRE format. use:(YYYY-MM-DD)")

        if datetime.strptime(expire_date, "%Y-%m-%d").date() < datetime.now().date():
            raise NameError("Expire Date Passed")

        return True,None

    @staticmethod


    # save and validate info and calculate total

    def save(p_id, product_name, brand, quantity, price, expire_date):
        try:
            ProductsController.validator(product_name, brand, quantity, price, expire_date)
            total = int(quantity) * int(price)
            product = Product(p_id,product_name,brand,quantity,price,expire_date,total)
            product_da = ProductsDataAccecc()
            product_da.save(product)
            return True, "Product Saved Successfully"
        except Exception as e:
            return False, f"{e}"

    @staticmethod


    #edit Feature


    def edit(p_id, product_name, brand, quantity, price, expire_date):
        try:
            ProductsController.validator(product_name, brand, quantity, price, expire_date)
            total = int(quantity) * int(price)
            product = Product(p_id,product_name,brand,quantity,price,expire_date,total)
            product_da = ProductsDataAccecc()
            product_da.edit(product)
            return True, "Product edited"
        except Exception as e:
            return False, f"{e}"

    @staticmethod


    #remove Feature


    def remove(p_id):
        try:
            product_da = ProductsDataAccecc()
            product_da.romove(p_id)
            return True, "Product Removed"
        except Exception as e:
            return False, f"Error removing Product{e}"

    # find all Feature


    @staticmethod
    def find_all():
        try:
            product_da = ProductsDataAccecc()
            products = product_da.find_all()
            return True, products
        except Exception as e:
            return False, f"Error find product {e}"

    @staticmethod
    def get_chart_data():
        try:
            product_da = ProductsDataAccecc()
            data = product_da.get_stock_data()

            names = [item[0] for item in data]
            quantities = [item[1] for item in data]

            return True, (names, quantities)
        except Exception as e:
            return False, f"Error getting chart data: {e}"





