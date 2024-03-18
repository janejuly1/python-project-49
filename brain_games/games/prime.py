from random import randint


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    result = []
    for i in range(1, (num + 1)):
        if num % i == 0:
            result.append(i)
    return len(result) == 2


def get_game_data():
    num = randint(0, 100)
    game_question = f'{num}'
    if is_prime(num):
        game_answer = "yes"
    else:
        game_answer = "no"
    return game_question, game_answer
