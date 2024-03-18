import random

RULE = "What is the result of the expression?"

def calculator():
    first, second = random.randint(1, 20), random.randint(1, 20)
    answer = f"{first} {random.choice('-*+')} {second}"
    return(answer, str(eval(answer)))