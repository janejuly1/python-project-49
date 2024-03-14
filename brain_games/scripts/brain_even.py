#!/usr/bin/env python3 -m brain_games.scripts
import random
import prompt


def question():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_answers = 3
    for _ in range(count_answers):
        num = random.randint(0, 100)
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = 'Correct!'
        wrong_answer = f"'{user_answer}' is wrong answer ;(. " \
                       f"Correct answer was " \
                       f"'{'yes' if num % 2 == 0 else 'no'}'." \
                       f"Let's try again, {name}!"
        if ((num % 2) == 0 and user_answer == 'yes') or \
                ((num % 2) != 0 and user_answer == 'no'):
            print(correct_answer)
            count_answers -= 1
        else:
            print(wrong_answer)
            break
        if count_answers == 0:
            print(f"Congratulations, {name}!")


def main():
    question()


if __name__ == '__main__':
    main()
