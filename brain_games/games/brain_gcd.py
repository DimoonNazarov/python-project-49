import random


LEFT_BORDER = 1
RIGHT_BORDER = 50
TASK = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(first, second):
    if second == 0:
        return first
    else:
        return calculate_gcd(second, first % second)


def question_and_answer():
    first = random.randint(LEFT_BORDER, RIGHT_BORDER)
    second = random.randint(LEFT_BORDER, RIGHT_BORDER)
    question = f'{first} {second}'
    correct_answer = calculate_gcd(first, second)
    return question, str(correct_answer)
