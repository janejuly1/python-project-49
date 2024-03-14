#!/usr/bin/env python3 -m brain_games.scripts
import prompt


def start(game):
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.CONDITION)
    count_answers = 3
    for _ in range(count_answers):
        game_question, game_answer = game.question()
        correct_answer = game_answer
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer).lower():
            print('Correct!')
            count_answers -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was "
                  f"'{correct_answer}'. "
                  f"Let's try again, {name}!")
            break
    if count_answers == 0:
        print(f"Congratulations, {name}!")
