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
        if game_data["HasScissors"]:
            game_data["Money"] += 5  
            print(f"Cutting grass with the scissors")
        else:
            game_data['Money'] += 1 
        print(f"You now have ${game_data['Money']}")

        
    if (user_input == 2):
        if game_data['Money'] >= 5:
            game_data['Money'] -= 5
            if game_data['HasScissors'] == True:
                print("You bought rusty scissors and can now cut grass faster!")
        else:
            print("You don't have enough money to buy scissors!")
    if(game_data["HasScissors"] == True):
        int(input(""" 
                    [1] buy a lawn mower

                    """))
    else:
        print("You")
        

    if(user_input == 3):
        game_data['quit'] == True
        print("You quit the game successfully")
        break
        