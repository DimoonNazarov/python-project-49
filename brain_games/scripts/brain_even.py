#!/usr/bin/env python3
import random
import prompt


def brain_noteven():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    k = 0
    for i in range(3):
        x = random.randint(1, 100)
        print(f"Question: {x}")
        answer = prompt.string("Your answer: ")
        if (x % 2 == 0 and answer == 'yes') or (x % 2 != 0 and answer == 'no'):
            print("Correct!")
            k = k + 1
            if k == 3:
                print("Congratulations, Bill!")
        else:
            print("'yes' is wrong answer ;(.'\n'Correct answer was 'no'. Let's try again, Bill!")
            break


if __name__ == '__main__':
    brain_noteven()
