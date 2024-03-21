import random


LEFT_BORDER = 1
RIGHT_BORDER = 20
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 1:
        return False
    index = 2
    while index <= num - 1:
        if num % index == 0:
            return False
        index += 1
    return True


def question_and_answer():
    question = random.randint(LEFT_BORDER, RIGHT_BORDER)
    answer = 'no'
    if is_prime(question):
        answer = 'yes'
    return question, answer
