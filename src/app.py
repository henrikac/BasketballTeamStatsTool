"""
Python Web Development Techdegree
Project 2 - Basketball Team Stats Tool
--------------------------------------
"""


from constants import PLAYERS, TEAMS
import os


MENU_OPTIONS = ['Display Team Stats', 'Quit']


panthers = dict()
bandits = dict()
warriors = dict()


def clear_console():
    """Clears the console"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_options(options):
    """Iterate over a collection and prints out the index and value"""
    for count, option in enumerate(options):
        print(f'{count + 1}) {option}')


def display_menu(title, options):
    """Displays a menu"""

    clear_console()
    print('BASKETBALL TEAM STATS TOOL\n')
    print(f'---- {title} ----\n')

    display_options(options)


def prompt_user(prompt_msg, num_options):
    """Prompts the user for an option (int) between 1 and 'num_options'
    Returns the user response
    """
    MIN_OPTION = 1
    MAX_OPTION = num_options

    while True:
        user_input = input(prompt_msg)

        try:
            user_input = int(user_input)

            if user_input < MIN_OPTION or user_input > MAX_OPTION:
                raise ValueError(f'Please only a option between {MIN_OPTION} and {MAX_OPTION}')
        except ValueError as err:
            print(f'Invald input: {err}')
        else:
            return user_input


def start():
    still_running = True

    while still_running:
        display_menu('MENU', MENU_OPTIONS)
        user_input = prompt_user('\nEnter option: ', len(MENU_OPTIONS))

        if user_input == 2:
            still_running = False
        elif user_input == 1:
            checking_teams = True

            while checking_teams:
                team_menu = TEAMS + ['Main menu']
                display_menu('TEAMS', team_menu)

                user_input = prompt_user('\nEnter team: ', len(team_menu))

                if user_input == 4:
                    checking_teams = False


"""
1. create intro / menu
2. add players to teams
3. display teams
"""


if __name__ == '__main__':
    start()
