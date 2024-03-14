#!/usr/bin/env python3 -m brain_games.scripts
import prompt


def wrong_answer_message(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was "
          f"'{correct_answer}'. "
          f"Let's try again, {name}!")


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.CONDITION)
    count_answers = 3
    for _ in range(count_answers):
        game_question, game_answer = game.question()
        correct_answer = game_answer
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == str(user_answer):
            print('Correct!')
            count_answers -= 1
        else:
            print(wrong_answer_message(user_answer, correct_answer, name))
            break
    if count_answers == 0:
        print(f"Congratulations, {name}!")
