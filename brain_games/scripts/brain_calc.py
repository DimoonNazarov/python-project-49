from brain_games.cli import welcome_user
import random
import prompt


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    k = 0
    for i in range(3):
        first, second = random.randint(1, 20), random.randint(1, 20)
        
        real_answer= f"Question: {first} {random.choice('-*+')} {second}"
        print(real_answer)
        answer = prompt.integer("Your answer: ")
        if  eval(real_answer) == int(answer):
            print("Correct!")
            k = k + 1
            if k == 3:
                print(f"Congratulations, {name}!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(real_answer)}'.")
            break

def main():
    calc()

if __name__ == "__main__":
    main()