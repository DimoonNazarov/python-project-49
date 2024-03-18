import prompt

def welcome_user(introduction=""):
    print("Welcome to the Brain Games!")
    if introduction:
        print(f"{introduction}")
    print()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def answer(question):
    print(f"Question: {question}")
    answer = prompt.string("Your answer: ")
    return answer