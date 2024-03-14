#!/usr/bin/env python3 -m brain_games.scripts
from random import randint


CONDITION = 'Find the greatest common divisor of given numbers.'


def gratest_division(num_1, num_2):
    divider = 1
    for i in range(1, min(num_1, num_2) + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            divider = i
    return divider


def question():
    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    game_question = f'{num_1} {num_2}'
    game_answer = gratest_division(num_1, num_2)
    return game_question, game_answer
