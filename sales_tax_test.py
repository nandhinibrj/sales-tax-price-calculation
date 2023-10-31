import unittest

from sales_tax.module import Item, Order
from sales_tax.module.sales_tax import SalesTax, calculate_sales_tax, is_product_imported, calculate_import_tax, round_float_price


class MyTestCase(unittest.TestCase):
    def test_receipt_after_tax(self):
        item_1 = Item("book", 1, 12.49)
        item_2 = Item("music CD", 1, 14.99)
        item_3 = Item("chocolate bar", 1, 0.85)
        order_1 = Order()
        order_1.set(item_1)
        order_1.set(item_2)
        order_1.set(item_3)
        print("--------Input 1---------")
        sales_tax_order_1 = SalesTax(order_1.item)
        sales_tax_order_1.print_order()
        sales_tax_order_1.calculate_sales_tax()
        print("-----------Output 1------------")
        sales_tax_order_1.print_receipt()
        self.assertEqual(sales_tax_order_1.is_product_exception("book"), True)
        self.assertEqual(sales_tax_order_1.is_product_exception("music CD"), False)
        self.assertEqual(sales_tax_order_1.is_product_exception("chocolate bar"), True)
        # Price after tax addition
        self.assertEqual(item_1.price, 12.49)
        self.assertEqual(item_2.price, 16.489)
        self.assertEqual(item_3.price, 0.85)
        self.assertEqual(round(sales_tax_order_1.receipt.total_sales_tax, 2), 1.5)
        self.assertEqual(round(sales_tax_order_1.receipt.total_cost, 2), 29.83)

    def test_sales_tax_calculation(self):
        self.assertEqual(calculate_sales_tax(11.25), 1.125)

    def test_imported_product(self):
        self.assertEqual(is_product_imported("imported bottle of perfume"), True)

    def test_import_tax_calculation(self):
        self.assertEqual(round_float_price(calculate_import_tax(47.50), 0.05), 2.45)

    def test_round_to_nearest(self):
        self.assertEqual(round_float_price(47.50, 0.05), 47.5)


if __name__ == '__main__':
    unittest.main()
