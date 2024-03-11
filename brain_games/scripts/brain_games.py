#!/usr/bin/env python3
import brain_games.cli


def main():
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    

if __name__ == '__main__':
    main()
