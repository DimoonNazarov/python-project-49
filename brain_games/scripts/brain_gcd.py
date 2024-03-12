#!/usr/bin/env python3
import random
import prompt
import math
import brain_games.cli


def gcd():
    name = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    k = 0
    for i in range(3):
        first, second = random.randint(1, 20), random.randint(1, 20)
        print(f"Question: {first} {second}")
        answer = prompt.integer("Your answer: ")
        if math.gcd(first, second) == answer:
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(.", end="")
            print(f"Correct answer was '{math.gcd(first, second)}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    gcd()
