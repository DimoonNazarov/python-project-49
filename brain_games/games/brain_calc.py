import random


LEFT_BORDER = 1
RIGHT_BORDER = 20
TASK = 'What is the result of the expression?'
OPERATORS = "-*+"


def question_and_answer():
    first = random.randint(LEFT_BORDER, RIGHT_BORDER)
    second = random.randint(LEFT_BORDER, RIGHT_BORDER)
    operator = random.choice(OPERATORS)
    question = f'{first} {operator} {second}'
    answer = eval(question)
    return question, str(answer)
