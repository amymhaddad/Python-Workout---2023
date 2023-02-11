# Number guessing game

import random


# version 1
def guess_game():
    random_num = random.randint(0, 100)

    while True:
        user_num = int(input("Enter a number: "))

        if user_num == random_num:
            print("Just right")
            break

        if user_num > random_num:
            print("Too high")

        elif user_num < random_num:
            print("Too low")
