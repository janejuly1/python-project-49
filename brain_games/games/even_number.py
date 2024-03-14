#!/usr/bin/env python3 -m brain_games.scripts
from random import randint


CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question():
    num = randint(0, 100)
    game_question = f'{num}'
    game_answer = is_even(num)
    return game_question, game_answer
