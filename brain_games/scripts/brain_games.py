#!/usr/bin/env python3
import brain_games.cli


def main():
    name = brain_games.cli.welcome_user()

    print('Hello, {0}!'.format(name))
    

if __name__ == '__main__':
    main()
