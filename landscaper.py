# game data
game_data = {
    "Money": 0,
    "HasScissors": False,
    "HasLawnmower": False,
    "HasBatteryLawnmower": False,
    "HasTeam": False,
    "quit": False,
}

# game functions
def cut_grass():
    if game_data['HasTeam']:
        game_data['Money'] += 250
    elif game_data['HasBatteryLawnmower']:
        game_data['Money'] += 100
    elif game_data['HasLawnmower']:
        game_data['Money'] += 50
    elif game_data['HasScissors']:
        game_data['Money'] += 5
    else:
        game_data['Money'] += 1
    print(f"You cut the grass and now have ${game_data['Money']}.")

def buy_scissors():
    if game_data['Money'] >= 5 and not game_data['HasScissors']:
        game_data['Money'] -= 5
        game_data['HasScissors'] = True
        print("You bought Rusty Scissors.")
    else:
        print("You couldn't afford Rusty Scissors.")
    print(f"You now have ${game_data['Money']}.")

def buy_lawnmower():
    if game_data['Money'] >= 25 and not game_data['HasLawnmower']:
        game_data['Money'] -= 25
        game_data['HasLawnmower'] = True
        print("You bought Old-timey Push Lawnmower.")
    else:
        print("You couldn't afford Old-timey Push Lawnmower.")
    print(f"You now have ${game_data['Money']}.")

def buy_battery_lawnmower():
    if game_data['Money'] >= 250 and not game_data['HasBatteryLawnmower']:
        game_data['Money'] -= 250
        game_data['HasBatteryLawnmower'] = True
        print("You bought Fancy Battery-powered Lawnmower.")
    else:
        print("You couldn't afford Fancy Battery-powered Lawnmower.")
    print(f"You now have ${game_data['Money']}.")

def hire_team():
    if game_data['Money'] >= 500 and not game_data['HasTeam']:
        game_data['Money'] -= 500
        game_data['HasTeam'] = True
        print("You hired a Team of Starving Students.")
    else:
        print("You couldn't afford to hire a Team of Starving Students.")
    print(f"You now have ${game_data['Money']}.")

def check_win():
    return game_data['HasTeam'] and game_data['Money'] >= 1000


while not game_data['quit'] and not check_win():
    user_input = input(""" What would you like to do today?
                            [1] Cut Grass
                            [2] Buy Rusty Scissors
                            [3] Buy Old-timey Push Lawnmower
                            [4] Buy Fancy Battery-powered Lawnmower
                            [5] Hire a Team of Starving Students
                            [6] Quit
                            """)
    
    if user_input == '1':
        cut_grass()

    elif user_input == '2':
        buy_scissors()

    elif user_input == '3':
        buy_lawnmower()

    elif user_input == '4':
        buy_battery_lawnmower()

    elif user_input == '5':
        hire_team()

    elif user_input == '6':
        game_data['quit'] = True


if check_win():
    print("Congratulations! You won the game.")
