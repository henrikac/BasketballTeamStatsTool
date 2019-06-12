"""
Python Web Development Techdegree
Project 2 - Basketball Team Stats Tool
--------------------------------------
"""


from constants import PLAYERS, TEAMS
import copy
import os
import random


MENU_OPTIONS = ['Display Team Stats', 'Quit']


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


def cleaned_data():
    """Cleans the PLAYERS data
    Converts the height into an integer
    Converts experience into a boolean (True/False)
    Converts guardians into a list of names
    Returns a set containing the cleaned PLAYERS data
    """
    players = copy.deepcopy(PLAYERS)

    for player in players:
        try:
            player["height"] = int(player["height"][:2])
        except ValueError as err:
            print(f'Error: {err}')
        else:
            if player["experience"] == "YES":
                player["experience"] = True
            else:
                player["experience"] = False

            player["guardians"] = player["guardians"].split(' and ')

    return players


def get_avg_height(team):
    """Calculates the average height of a team"""
    return sum([player["height"] for player in team]) / len(team)


def extract_players(players, experienced):
    """Extracts players depending on their experience
    Returns the extracted players
    """
    return [player for player in players if player["experience"] == experienced]


def create_team(players):
    """Creates a balanced team with equal numbers of experiencd and inexperienced players
    Players added to the team is randomly picked
    Returns the created team and the remaining players
    """
    players = players

    exp_players = extract_players(players, True)
    inexp_players = extract_players(players, False)

    # selects 6 players randomly
    # 3 experienced players and 3 inexperienced players
    team = random.sample(exp_players, k=3) + random.sample(inexp_players, k=3)

    # removes the picked players from the list of available players
    players = [player for player in players if player not in team]

    return (team, players)


def generate_teams():
    """Generates the teams"""
    players = cleaned_data()

    panthers, players = create_team(players)
    bandits, players = create_team(players)
    warriors, players = create_team(players)

    return (panthers, bandits, warriors)


def display_team_stats(team):
    """Display the stats of a team"""
    exp_players = [player for player in team if player["experience"] == True]
    num_exp_players = len(exp_players)
    
    print(f'Total players: {len(team)}')
    print(f'Average height: {get_avg_height(team)}')
    print(f'Number of experienced players: {num_exp_players}')
    print(f'Number of inexperienced players: {len(team) - num_exp_players}')


def display_names(title, names_list):
    """Display names in a list"""
    print(f'\n{title}:')
    print(f'\t{", ".join(names_list)}')


def display_team(team_name, team):
    """Display a team"""
    players = [player["name"] for player in team]
    guardians = [guardian for player in team for guardian in player["guardians"]]

    clear_console()
    print(f'TEAM: {team_name}')
    print('----------------')
    display_team_stats(team)
    display_names('Players on team', players)
    display_names('Guardians', guardians)
    input('\nPress ENTER to continue...')


def start():
    """Main function that runs the program"""
    still_running = True
    teams = generate_teams()

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
                else:
                    idx = user_input - 1
                    display_team(TEAMS[idx], teams[idx])


if __name__ == '__main__':
    start()

