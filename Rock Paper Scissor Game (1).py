"""
WORKFLOW OF PROJECT:
1- input from user(rock, paper, scissor)
2- computer choice(computer will choose randomly not conditionally)
3- Result print

cases:
A- rock
rock-rock=tie
rock-paper=paper win
rock- scissor=rock win

B- paper
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor win

C-scissor
scissor-scissor=tie
scissor-rock=rock win
scissor-paper=scissor win

"""

import random 
item_list =["rock","paper","scissor"]

user_choice =input("Enter your move = rock,paper,scissor=")
comp_choice =random.choice(item_list)

print(f"user choice ={user_choice},Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper cover rock =computer win")
    else:
        print("rock smashes scissor = you win")

elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper = computer win") 
    else:
        print("paper cover rock = you win") 

elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissor cuts paper = you win")
    else:
        print("rock smashes scissor = computer win")
            