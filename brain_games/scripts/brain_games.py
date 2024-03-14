#!/usr/bin/env python3 -m brain_games.scripts
from ..cli import welcome_user


def greet():
    print("Welcome to the Brain Games!")
    print(f'Hello, {welcome_user()}')


def main():
    greet()


if __name__ == '__main__':
    main()
