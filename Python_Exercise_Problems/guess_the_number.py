"""
Корисникот замислува еден број помеѓу 1 и 1000000000. Потоа на влез
програмата кажува број а корисникот треба да избере дали бројот е точен,
поголем или помал од неговиот замислен број. Играта завршува кога
програмата ќе го погоди бројот кој го замислил корисникот.
"""
from random import randint


def guess_num(number):
    lowerBound, upperBound = 0, 1000000000
    numGuesses = 0
    while True:
        guess = randint(lowerBound, upperBound)
        print(f"Is your number {guess}?")
        if number > guess:
            print("Larger")
            lowerBound = guess
            numGuesses += 1
        elif number < guess:
            print("Smaller")
            upperBound = guess
            numGuesses += 1
        else:
            return f"Correct guess, took {numGuesses} tries"


if __name__ == '__main__':
    number = randint(0, 1000000000)
    print(guess_num(number))