from datetime import datetime
import re as rex


class Product(object):

    def __init__(self, product_id: int, product_name: str):
        self.product_id = product_id
        self.product_name = product_name

    def __str__(self):
        return '{0},{1}'.format(self.product_id, self.product_name)

    def __repr__(self):
        return "{0}:[{1}]".format("Product ", str(self.__dict__()))

    def __dict__(self):
        return {"product_id": self.product_id, "product_name": self.product_name}

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if type(product_id) is not int:
            raise TypeError("Requires integer!")
        if product_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = str(product_name).strip()


class InventoryCount(object):

    def __init__(self, product: Product, count: int):
        ""
        self.product = product
        self.count = count

    def __str__(self):
        return '{0},{1},{2}'.format(self.product.product_id, self.product.product_name, self.count)

    def __repr__(self):
        return "{i}:[{p}, {c}:{cv}]".format(i="InventoryCount",
                                            p=self.product.__repr__(),
                                            c="count",
                                            cv=self.count)

    # Add properties and validation
    # product is Product
    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product):
        self.__product = product

    # count >= 0
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if type(count) is not int:
            raise TypeError("Requires integer!")
        if count < 0:
            raise ValueError("Requires value greater than or equal to zero!")
        else:
            self.__count = count


class Inventory(object):
    def __init__(self, inventory_id: int, inventory_date: datetime.date, inventory_counts: InventoryCount = [None]):
        self.inventory_id = inventory_id
        self.inventory_date = inventory_date
        if inventory_counts is not None:
            self.inventory_counts = inventory_counts

    def __str__(self):
        return '{0},{1},{2}'.format(self.inventory_id, self.inventory_date, self.inventory_counts)

    def __repr__(self):
        return "{i}: [{idt} {idtv}, {iid} {iidv}, {ic}]:".format(i="Inventory",
                                                                   idt='Inventory Date:',
                                                                   idtv=self.inventory_date,
                                                                   iid='Inventory ID:',
                                                                   iidv=self.inventory_id,
                                                                   ic=self.inventory_counts.__repr__())

    # Add properties and validation
    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        # inventory_id > 0
        if type(inventory_id) is not int:
            raise TypeError("Requires integer!")
        if inventory_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__inventory_id = inventory_id

    @property
    def inventory_date(self):
        return self.__inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        # date is datetime type
        if rex.match(r"\d\d\d\d-\d\d-\d\d", str(inventory_date)) is None:
            raise ValueError('Requires date format YYYY-MM-DD')
        else:
            self.__inventory_date = inventory_date

    # inventory_counts is Inventory_Count object
    @property
    def inventory_counts(self):
        return self.__inventory_counts

    @inventory_counts.setter
    def inventory_counts(self, inventory_counts):
        if type(inventory_counts) is not int:
            raise TypeError("Requires integer!")
        if inventory_counts <= 0:
            raise ValueError("Requires value greater than or equal to zero!")
        else:
            self.__inventory_counts = inventory_counts


if __name__ == '__main__':
    p1 = Product(11101003, "ProdA")
    p2 = Product(11101004, "ProdB")

    ic = InventoryCount(p1, 420)

    # inv = Inventory(366, '2019-04-11', ic)
    print(str(ic))

    # p1 = Product(11101011, "ProdA")
    # p2 = Product(11101012, "ProdB")
    # ic1 = InventoryCount(p1, 15)
    # print(ic1)
    # print(repr(ic1))

    # p1 = Product(11101011, "Mouse")
    # p2 = Product(11101012, "Keyboard")
    # print(p1)

    # p1 = Product(1110101, "ProdA")
    # p2 = Product(1110102, "ProdB")
    # ic1 = InventoryCount(p1, 15)
    # ic2 = InventoryCount(p2, 45)
    # invJan0119 = Inventory(1, '2020-01-01', [ic1, ic2])
    # for ic in invJan0119.inventory_counts:
    #     print('Jan 2019 -', ic.product.product_name, ' = ', ic.count)
    #

    # try:
    #     Product('A', "Alpha")
    # except Exception as e:
    #     print(e)
    # try:
    #     Product(1.2, "Float")
    # except Exception as e:
    #     print(e)
    # try:
    #     Product(0, "Zero")
    # except Exception as e:
    #     print(e)
    # try:
    #     Product(-1, "LT Zero")
    # except Exception as e:
    #     print(e)
