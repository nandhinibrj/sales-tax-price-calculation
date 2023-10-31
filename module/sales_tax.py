import math

from sales_tax.module.Receipt import Receipt
from sales_tax.module.item import Item
from sales_tax.module.order import Order


def calculate_sales_tax(price: float) -> float:
    sales_tax = price * 0.10
    return sales_tax


def is_product_imported(product: str) -> bool:
    return "import" in product.lower()


def calculate_import_tax(price: float) -> float:
    import_tax = (price * 5) / 100
    return round_float_price(import_tax, 0.05)


def round_float_price(price: float, round_digit: float) -> float:
    base = .05
    return math.ceil(price / base) * base


class SalesTax:

    def __init__(self, order: Order = None):
        if order is None:
            order = []
        self.exception_goods = ["chocolate", "book", "pill"]
        self.order = order
        if order is not None:
            self.receipt = Receipt(self.order)

    def is_product_exception(self, product) -> bool:
        if any(word in product.lower() for word in self.exception_goods):
            return True
        return False

    def add_sales_tax(self, index: int, item: Item):
        sales_tax = calculate_sales_tax(item.price)
        item.price = item.price + sales_tax
        item.sales_tax = item.sales_tax + sales_tax
        self.receipt.order.__setitem__(index, item)

    def add_import_tax(self, index: int, item: Item):
        import_tax = calculate_import_tax(item.price)
        item.price = item.price + import_tax
        item.sales_tax = item.sales_tax + import_tax
        self.receipt.order.__setitem__(index, item)

    def calculate_sales_tax(self):
        for index, item in enumerate(self.order):
            if item is not None:
                if not self.is_product_exception(item.name):
                    self.add_sales_tax(index, item)
                if is_product_imported(item.name):
                    self.add_import_tax(index, item)

    def print_sales_tax(self):
        for item in self.receipt.order:
            print(f"{item.name} - {item.sales_tax}")

    def add_overall_sales_tax(self):
        self.receipt.total_sales_tax = sum(item.sales_tax for item in self.receipt.order)

    def add_total_cost(self):
        self.receipt.total_cost = sum(item.price for item in self.receipt.order)

    def print_order(self):
        for item in self.order:
            if item is not None:
                print(f"{item.quantity} {item.name} at {format(item.price, '.2f')}")
                # f"{format(item.price, '.2f')}")

    def print_receipt(self):
        for item in self.receipt.order:
            if item is not None:
                print(f"{item.quantity} {item.name} at {format(item.price, '.2f')}")
                # f"{format(item.price, '.2f')}")
        self.add_overall_sales_tax()
        self.add_total_cost()
        print(f"Sales Taxes: {format(self.receipt.total_sales_tax, '.2f')}")
        print(f"Total: {format(self.receipt.total_cost, '.2f')}")
