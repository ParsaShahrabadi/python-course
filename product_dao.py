import sqlite3


class ProductsDataAccecc:

    def save(self, product):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into products (p_id,product_name,brand,quantity,price,expire_date,total)" "values (?, ?, ?, ?, ?, ?, ?)" ,
                           [product.p_id,
                            product.product_name,
                            product.brand,
                            product.quantity,
                            product.price,
                            product.expire_date,
                            product.total
                            ])

            connection.commit()

    def edit(self, product):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("update products set product_name=?, brand=? ,quantity=?, price=?,expire_date=?,  total=? where p_id=?",
                           [
                            product.product_name,
                            product.brand,
                            product.quantity,
                            product.price,
                            product.expire_date,
                            product.total,
                            product.p_id
                            ])
            connection.commit()

    def romove(self, p_id):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from products where p_id=?", [p_id])
            connection.commit()

    def find_all(self):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from products order by p_id")
            return cursor.fetchall()

    def get_stock_data(self):
        with sqlite3.connect("smc_db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT product_name, quantity FROM products")
            return cursor.fetchall()