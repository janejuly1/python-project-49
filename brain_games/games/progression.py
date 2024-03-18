from random import randint, choice


QUESTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_progression(question_progression, elem):
    index = question_progression.index(elem)
    question_progression[index] = '..'

    return ' '.join(str(element) for element in question_progression)


def get_game_data():
    first_el = randint(1, 10)
    question_progression = [first_el]
    step = randint(1, 10)
    i = first_el
    while len(question_progression) < PROGRESSION_LENGTH:
        i += step
        question_progression.append(i)
    elem = choice(question_progression)
    game_question = f'{get_progression(question_progression, elem)}'
    game_answer = elem
    return game_question, game_answer
