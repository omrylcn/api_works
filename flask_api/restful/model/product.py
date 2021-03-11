product_list = []


def get_last_id():
    if product_list:
        last_product = product_list[-1]

    else:
        return 1

    return last_product.id + 1


class Product:

    def __init__(self, id, category_id, product_name,
                 quantity_per_unit, unit_price, units_in_stock):

        #self.id = get_last_id()
        self.id = id
        self.category_id = category_id
        self.product_name = product_name
        self.quantity_per_unit = quantity_per_unit
        self.unit_price = unit_price
        self.units_in_stock = units_in_stock

        self.is_publish = False

    @property
    def data(self):
        return {
            "id": self.id,
            "category_id": self.category_id,
            "product_name": self.product_name,
            "quantity_per_unit": self.quantity_per_unit,
            "unit_price": self.unit_price,
            "units_in_stock": self.units_in_stock
        }
