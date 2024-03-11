#!/usr/bin/env python3
import random
import math
import prompt
import brain_games.cli


def is_prime(number: int) -> bool:
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
        random_number = random.randint(1, 100)
        print("Question:", random_number)
        answer = prompt.string("Your answer: ")
        if (is_prime(random_number) and answer == 'yes') or (not is_prime(random_number) and answer == 'no'):
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'yes' is wrong answer ;(.Correct answer was 'no'. Let's try again, {name}!")
            break


if __name__ == "__main__":
    prime()
