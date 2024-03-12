import random
import prompt
import brain_games.cli


def progression():
    name = brain_games.cli.welcome_user()
    print('What number is missing in the progression?')
    k = 0
    for i in range(3):
        print("Question: ", end="")
        start, delta = random.randint(1, 20), random.randint(1, 20)
        hidden_index = random.randint(0, 9)
        for i in range(10):
            if i == hidden_index:
                print("..", end=" ")
                hidden_number = start + i * delta
            else:
                print(start + i * delta, end=" ")
        print()
        answer = prompt.integer("Your answer: ")
        if answer == hidden_number:
            print("Correct!")
            k += 1
            if k == 3:
                print(f"Congratulations, {name}!")
                break
        else:
            print(f"'{answer}' is wrong answer ;(.", end="")
            print(f"Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    progression()
