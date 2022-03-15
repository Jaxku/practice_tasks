def game_time():

    import random #Computer gets to choose randomly what it picks
    choices = ["rock", "paper", "Scissors"]
    computer = random.choice(choices)

    player_input = input("Do you want to play Paper, Scissors or ROCK!: ")
    print("computer: ", computer)
    print(f"{player_name} picked: player_input)
    return

#Main Function
player_name = input("What is your name: ")
ready_to_play = input(f"Hello {player_name} are you ready to play paper, scissors, rock! (Y/N)").upper()
if ready_to_play != "Y":
    print("this code works so far")
