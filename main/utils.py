
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

if __name__ == '__main__':
    op = Category('Фрукты', 'Сладкие, спелые и свежие', [{'Яблоки':[{'pay': 10, }], 'Апельсины', 'Персики'}])
    #op.input_product()
    print(op.products_return)
