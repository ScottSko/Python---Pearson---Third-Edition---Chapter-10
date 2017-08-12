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

    def __str__(self):

        return self.__desc + \
               "\n"+self.__units + \
               "\n"+str(self.__price)

    #you can also write a method that just returns every attribute you want, without needing to name it __str__
    #the difference is that with the __str__, you can simply pass the object to the print function, rather than call a method.
