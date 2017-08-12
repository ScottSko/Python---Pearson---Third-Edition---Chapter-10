class Pet:

    def __init__(self, name, animal_type, age):

        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):

        self.__name = name

    def set_animal_type(self, animal_type):

        self.__animal_type = animal_type

    def set_age(self, age):

        self.__age = age

    def get_name(self):

        return self.__name

    def get_animal_type(self):

        return self.__animal_type

    def get_age(self):

        return self.__age


def main():

    n = "Spot"
    t = "Dog"
    a = "2 years"

    pet = Pet(n, t, a)

    name = pet.get_name()
    type = pet.get_animal_type()
    age = pet.get_age()

    print("The pet's name is:", name)
    print(name, "is a", type)
    print(name, "the", type, "is", age, "old")

main()