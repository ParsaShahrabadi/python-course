import re
from datetime import datetime, date, time
from product_modell import Products
from product_dao import ProductDataAccecc


class ProductsController:
    @staticmethod


    #validating products information


    def validator(name, brand, quantity, price, expire_date,):

        if not re.match("^[a-zA-Z\s]{3,30}$", name):
            raise ValueError("Invalid name")

        if not re.match("^[a-zA-Z0-9\s]{3,30}$", brand):
            raise ValueError("Invalid brand")

        if not price > 0:
            raise ValueError("Invalid price")

        if not quantity > 0:
            raise ValueError("Invalid quantity")

        try:
            datetime.strptime(expire_date, '%Y-%m-%d')
        except ValueError:
            raise NameError("Invalid expire format: yyyy-mm-dd")

        if datetime.now().date() > datetime.strptime(expire_date, '%Y-%m-%d'):
            raise NameError("Expier Date Padded")

        return True

    @staticmethod


    # save and validate info and calculate total


    def validate_and_save(id, name, brand, quantity, price, expire_date):

            try:
                ProductsController.validator(name, brand, quantity, expire_date, price)
            except Exception as e:
                return False, f"{e}"

            total = quantity * price

            try:
                product = Products(id,name,brand,quantity,expire_date,price,total)
                product_da = ProductDataAccecc()
                product_da.save(product)
                return True, "Product Saved Successfully"

            except Exception as e:
                return False, f"Failed to save product: {e}"

    @staticmethod


    #edit Feature


    def edit(id, name, brand, quantity, price, expire_date):

            try:
                ProductsController.validator(name, brand, quantity, expire_date, price)
            except Exception as e:
                return False, f"{e}"

            total = quantity * price

            try:
                product = Products(id,name,brand,quantity,expire_date,price,total)
                product_da = ProductDataAccecc()
                product_da.edit(product)
                return True, "Product edited"

            except Exception as e:
                return False, f"Error edit product: {e}"

    @staticmethod


    #remove Feature


    def remove(id):
        try:
            product_da = ProductDataAccecc()
            product_da.romove(id)
            return True, "Product Removed"
        except Exception as e:
            return False, f"Error removing Product{e}"

    # find all Feature


    @staticmethod
    def find_all():
        try:
            product_da = ProductDataAccecc()
            return True, product_da.find_all()
        except Exception as e:
            return False, f"Error find product {e}"





