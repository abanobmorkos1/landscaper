game_data = {
    "Money": 0,
    "HasScissors": False,
    "quit": True,
}
########## beginging of the prompt 
while(True):
    user_input = int(input(""" What would you like to do today?
                            [1] Cut Grass
                           
                            [2] Spend $5 to buy rusty scissors to cut grass faster
                           
                            [3] Take the day off
                            """))
    if (user_input == 1):
        game_data["Money"] += 1
        print(f'You now have ${game_data["Money"]}')
