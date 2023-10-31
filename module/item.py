class Item:

    def __init__(self, name: str, quantity: int, price: float, sales_tax: float = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sales_tax = sales_tax

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def price(self):
        return self._price

    @property
    def sales_tax(self):
        return self._sales_tax

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @name.setter
    def name(self, value):
        self._name = value

    @price.setter
    def price(self, value):
        self._price = value

    @sales_tax.setter
    def sales_tax(self, value):
        self._sales_tax = value
