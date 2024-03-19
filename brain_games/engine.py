import prompt


RUNS_COUNT = 3


def start(game):
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUESTION)
    count_rounds = RUNS_COUNT
    for _ in range(count_rounds):
        game_question, game_answer = game.get_game_data()
        correct_answer = game_answer
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer).lower():
            print('Correct!')
            count_rounds -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was "
                  f"'{correct_answer}'. "
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
