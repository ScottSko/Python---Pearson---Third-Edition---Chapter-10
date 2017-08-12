class Car:

    def __init__(self, year, make):

        self.__year = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):

        self.__speed += 5

    def brake(self):

        self.__speed -= 5

    def get_speed(self):

        return self.__speed

def main():

    speed = 0

    year = 1990

    make = "Toyota"

    car1 = Car(year, make)

    for x in range(5):
        car1.accelerate()
        print("The car is now moving at", car1.get_speed(), "miles per hour")

    print("The car has finished accelerating and will now slow down.")

    for x in range(5):
        car1.brake()
        print("The car is now moving at", car1.get_speed(), "miles per hour")

    print("The car is now stopped.")


main()