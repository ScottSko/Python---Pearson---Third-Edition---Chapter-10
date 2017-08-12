class Car:

    def __init__(self):

        self.__speed = 0

    def go(self, velocity):

        self.__speed = velocity

    def __str__(self):

        self.__speed = str(self.__speed)

        return self.__speed

def main():

    my_car = Car()

    print(my_car)

    my_car.go(60)

    print(my_car)

main()