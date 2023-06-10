--the code

import time

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock,paper,Scissors: ").lower()

print("you picked " +player)
time.sleep(1)
print("The computer picked " +computer)
if player == computer:
    print("nobody won :(")

elif player == "rock":
    if computer == "paper":
        print("you lose")

elif player == "paper":
    if computer == "rock":
        print("you WIN")

elif player == "scissors":
    if computer == "rock":
        print("you lose")

elif player == "rock":
    if computer == "scissors":
        print("you win ")

elif player == "rock":
    if computer == "paper":
        print("you lose")

elif player == "paper":
    if computer == "scissors":
        print("you lose")
