class Category:
    """Описание категории товаров"""
    name = str
    description = str
    products = list
    sum_products = 3
    unique_product = 1

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


    def products_return(self):
        result = ', '.join(self.products)
        return result

class Product:
    """Описание конкретного товара"""
    name = str
    description = str
    pay = float
    in_stock = int

    def __init__(self, name, description, pay, in_stock):
        self.name = name
        self.description = description
        self.pay = pay
        self.in_stock = in_stock
