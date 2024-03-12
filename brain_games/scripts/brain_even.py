#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import welcome_user


def even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    k = 0
    for i in range(3):
        rn = random.randint(1, 100)
        print(f"Question: {rn}")
        answ = prompt.string("Your answer: ")
        if (rn % 2 == 0 and answ == 'yes') or (rn % 2 != 0 and answ == 'no'):
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print("'yes' is wrong answer ;(.", end="")
            print(f"Correct answer was 'no'. Let's try again, {name}!")
            break


if __name__ == '__main__':
    even()
