class Personal:

    def __init__(self, name, address, age, phone_number):

        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self):

        return self.__name

    def get_address(self):

        return self.__address

    def get_age(self):

        return self.__age

    def get_phone_number(self):

        return self.__phone_number

    def set_name(self, name):

        self.__name = name

    def set_address(self, address):

        self.__address = address

    def set_age(self, age):

        self.__age = age

    def set_phone_number(self, phone_number):

        self.__phone_number = phone_number


def main():

    n1 = input("What is your name? ")
    ad1 = input("What is your address? ")
    a1 = int(input("What is your age? "))
    pn1 = input("What is your phone number? ")

    p1 = Personal(n1, ad1, a1, pn1)

    print(p1.get_name())
    print(p1.get_address())
    print(p1.get_age())
    print(p1.get_phone_number())

main()