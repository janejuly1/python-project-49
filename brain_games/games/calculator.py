from random import randint, choice


QUESTION = 'What is the result of the expression?'


def carry_out_calculation(num_1, num_2, operator):
    match operator:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "*":
            return num_1 * num_2


def get_game_data():
    num_1 = randint(0, 100)
    num_2 = randint(0, 100)
    operator = choice(('+', '-', '*'))
    game_question = f'{num_1} {operator} {num_2}'
    game_answer = carry_out_calculation(num_1, num_2, operator)
    return game_question, game_answer
