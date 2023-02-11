#Number guessing game

import random 

def guess_game():
    random_num = random.randint(0, 4)
    user_num = int(input("Enter a number: "))

    while user_num != random_num:
        if user_num > random_num:
            print("Too high")

        elif user_num < random_num:
            print("Too low")

        user_num = int(input("Enter a number"))

    print("Just right")

print(guess_game())
