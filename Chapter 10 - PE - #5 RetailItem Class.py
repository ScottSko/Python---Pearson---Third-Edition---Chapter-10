class RetailItem:

    def __init__(self, desc, units, price):

        self.__desc = desc
        self.__units = units
        self.__price = price

    def get_desc(self):

        return self.__desc

    def get_units(self):

        return self.__units

    def get_price(self):

        return self.__price

    def set_desc(self, desc):

        self.__desc = desc

    def set_units(self, units):

        self.__units = units

    def set_price(self, price):

        self.__price = price


def main():

    i1_desc = "Jacket"
    i1_units = "12"
    i1_price = 59.95

    item1 = RetailItem(i1_desc, i1_units, i1_price)

    print(item1.get_desc())
    print(item1.get_units())
    print(item1.get_price())

main()