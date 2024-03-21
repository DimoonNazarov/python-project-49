import brain_games.cli
import prompt

COUNT_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = brain_games.cli.welcome_user()
    print(game.TASK)

    counter = 0
    while counter < COUNT_OF_ROUNDS:
        question, correct_answer = game.question_and_answer()
        print(f'Question: {question}')
        user_anser = prompt.string('Your answer: ')
        if user_anser == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"'{user_anser}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f'Congratulations, {user_name}!')
