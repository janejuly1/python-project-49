#!/usr/bin/env python3 -m brain_games.scripts
from random import randint


CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    if len(result) == 2:
        return 'yes'
    else:
        return 'no'


def question():
    num = randint(0, 100)
    game_question = f'{num}'
    game_answer = prime(num)
    return game_question, game_answer
