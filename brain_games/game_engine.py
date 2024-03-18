import brain_games.cli

COUNT_OF_ROUNDS = 3


def engine(game):
    player_name = brain_games.cli.welcome_user(game.RULE)

    for i in range(COUNT_OF_ROUNDS):
        question, correct = game.run_game()
        answer = answer(question)
        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {player_name}!")
            return
        print("Correct")
    print(f"Congratulations, {player_name}!")
