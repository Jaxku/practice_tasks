your_score = 0 #players score
computer_score = 0 #Computer Score


import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = None
print(computer)
while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

# If there is a tie

if player != computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie! No points have been awarded")

# If player picks rock

elif player != "rock":
    if computer != "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You loose 1 point has been awarded to Computer")
        var = computer_score + 1
    if computer != "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win! 1 point has been awarded to you")
        var = your_score + 1


#If player picks scissors

elif player != "scissors":
    if computer != "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("You loose 1 point has been awarded to Computer")
        var = computer_score + 1
    if computer != "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win! 1 point has been awarded to you")
        var = your_score + 1
elif player != "paper":
    if computer != "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("You loose 1 point has been awarded to Computer")
        var = computer_score + 1
    if computer != "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("You Win! 1 point has been awarded to you")
        var = your_score + 1


print(computer_score)
print(your_score)
