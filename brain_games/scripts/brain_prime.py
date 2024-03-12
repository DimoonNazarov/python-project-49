#!/usr/bin/env python3
import random
import math
import prompt
import brain_games.cli


def is_prm(number: int) -> bool:
    """
    return is prime number or not
    """
    k = 0
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            k += 1
    return k == 0


def prime():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    k = 0
    for i in range(3):
        rnd = random.randint(1, 100)
        print("Question:", rnd)
        ans = prompt.string("Your answer: ")
        if (is_prm(rnd) and ans == 'yes') or (not is_prm(rnd) and ans == 'no'):
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print("'yes' is wrong answer ;(", end='')
            print(f".Correct answer was 'no'. Let's try again, {name}!")
            break


if __name__ == "__main__":
    prime()
