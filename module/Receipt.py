from sales_tax.module.order import Order


class Receipt:

    def __init__(self, order: Order, total_sales_tax: float = 0, total_cost: float = 0):
        self.order = order
        self.total_sales_tax = total_sales_tax
        self.total_cost = total_cost

    @property
    def total_sales_tax(self):
        return self._total_sales_tax

    @property
    def total_cost(self):
        return self._total_cost

    @total_sales_tax.setter
    def total_sales_tax(self, value):
        self._total_sales_tax = value

    @total_cost.setter
    def total_cost(self, value):
        self._total_cost = value
