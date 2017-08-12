import random

class Coin:

    def __init__(self):

        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup

def main():

    Heads = 0
    Tails = 0

    my_coin = Coin()

    print(my_coin.sideup)

    #print("This side is up:", my_coin.get_sideup())

    #print("I am tossing the coin . . .")
    #my_coin.toss()

    #print("This side is up:", my_coin.get_sideup())

    for x in range(50):
        my_coin.toss()
        if my_coin.get_sideup() == "Heads":
            Heads += 1
        else:
            Tails += 1

    print("After 50 coin tosses, the results were:")
    print("--------------")
    print("Heads:", Heads)
    print("Tails:", Tails)

main()