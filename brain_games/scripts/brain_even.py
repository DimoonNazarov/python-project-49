#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import welcome_user


def brain_noteven():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    k = 0
    for i in range(3):
        random_number = random.randint(1, 100)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        if (random_number % 2 == 0 and answer == 'yes') or (random_number % 2 != 0 and answer == 'no'):
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'yes' is wrong answer ;(.\nCorrect answer was 'no'. Let's try again, {name}!")
            break


def main():
    brain_noteven()


if __name__ == '__main__':
    main()
