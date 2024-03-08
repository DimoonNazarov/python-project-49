#!/usr/bin/env python3
import random
import prompt
import brain_games.cli


def calc():
    name = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    k = 0
    for i in range(3):
        first, second = random.randint(1, 20), random.randint(1, 20)
        print("Question: ", end='')
        real_answer = f"{first} {random.choice('-*+')} {second}"
        print(real_answer)
        answer = prompt.integer("Your answer: ")
        if eval(real_answer) == answer:
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(real_answer)}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    calc()


if __name__ == "__main__":
    main()
