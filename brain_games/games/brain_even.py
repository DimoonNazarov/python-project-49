import random


LEFT_BORDER = 1
RIGHT_BORDER = 999
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def question_and_answer():
    question = random.randint(LEFT_BORDER, RIGHT_BORDER)
    correct_answer = 'no'
    if is_even(question):
        correct_answer = 'yes'
    return question, correct_answer
