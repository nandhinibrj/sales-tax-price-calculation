from typing import List

from sales_tax.module.item import Item


class Order:

    def __init__(self, item: List[Item] = None):
        if item is None:
            item = []
        self._item = item

    @property
    def item(self):
        return self._item

    def set(self, product):
        self._item.append(product)

    def __setitem__(self, key, value):
        self._item.insert(key, value)

    def __getitem__(self, index):
        return self._item[index]

