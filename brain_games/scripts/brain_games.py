#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_noteven


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    brain_noteven()



if __name__ == '__main__':
    main()
