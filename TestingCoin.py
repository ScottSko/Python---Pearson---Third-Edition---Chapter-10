import random
import coin

def main():

    coin1 = coin.Coin()

    print(coin1.get_sideup())

    flip(coin1)

    print(coin1.get_sideup())

    coin_status = str(coin1)

    print(coin_status)

def flip(coin):
    coin.toss()

main()