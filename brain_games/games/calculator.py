#!/usr/bin/env python3 -m brain_games.scripts
from random import randint, choice


CONDITION = 'What is the result of the expression?'


def expressions(num_1, num_2, operator):
    match operator:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2


def question():
    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    operator = choice(('+', '-', '*'))
    game_question = f'{num_1} {operator} {num_2}'
    game_answer = expressions(num_1, num_2, operator)
    return game_question, game_answer
