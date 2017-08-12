import retailitem

class CashRegister:

    def __init__(self):

        self.__list = []

    def purchase_item(self, retail_object):

        self.__list.append(retail_object)

    def get_total(self):

        total = 0

        for x in self.__list:
            total += x.get_price()

        return total

    def show_items(self):

        for x in self.__list:
            print(x)

    def clear(self):

        self.__list = []

    #def __str__(self):

        #return self.__list



def main():

    desc = "Hello"
    units = "5"
    price = 60

    r_i = retailitem.RetailItem(desc, units, price)
    r_2 = retailitem.RetailItem(desc, units, price)

    #print(r_i)

    c_r = CashRegister()

    c_r.purchase_item(r_2)

    c_r.purchase_item(r_i)

    print(c_r.get_total())
    print(c_r.show_items())

    c_r.clear()

    print(c_r.show_items())

    #print(r_i)

main()







