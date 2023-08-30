game_data = {
    "Money": 0,
    "quit": True,
}

while(True):
    user_input = int(input(""" What would you like to do today?
                            [1] Spend all day cutting grass with your teeth for $1 
                            [2] Spend $5 to buy rusty scissors to cut grass faster
                            [3] take the day off
                            """))
    if (user_input == 1):
        game_data['Money'] += 1
        print(f"You now have ${game_data['Money']}")    
    
    if (user_input == 2):
        game_data['Money'] -= 5
        print(f"You bought a rusty scissors , you know have ${game_data['Money']}")

    if (user_input == 3):
        print("You Quit the game successfully")
        break
