#!/usr/bin/env python3 -m brain_games.scripts
from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_game_data():
    num = randint(0, 100)
    game_question = f'{num}'
    game_answer = "yes" if is_even(num) else "no"
    return game_question, game_answer
