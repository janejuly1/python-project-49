#!/usr/bin/env python3 -m brain_games.scripts
from random import randint, choice


CONDITION = 'What number is missing in the progression?'


def progression(question_progression, elem):
    index = question_progression.index(elem)
    question_progression[index] = '..'

    return ' '.join(str(element) for element in question_progression)


def question():
    first_el = randint(1, 10)
    question_progression = [first_el]
    step = randint(1, 10)
    i = first_el
    while len(question_progression) < 10:
        i += step
        question_progression.append(i)
    elem = choice(question_progression)
    game_question = f'{progression(question_progression, elem)}'
    game_answer = elem
    return game_question, game_answer
