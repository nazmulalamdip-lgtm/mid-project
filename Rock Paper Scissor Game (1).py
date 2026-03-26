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

user_score=0
computer_score=0

total_rounds=int(input("How many rounds do you want to play?"))

for round_num in range(1, total_rounds +1):
    print(f" Round{round_num}")
user_choice =input("Enter your move = rock,paper,scissor=").lower()
comp_choice =random.choice(item_list)

print(f"user choice ={user_choice},Computer choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same: = Match Tie")

elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper cover rock =computer win")
        computer_score +=1
    else:
        print("rock smashes scissor = you win")
        user_score+=1

elif user_choice=="paper":
    if comp_choice=="scissor":
        print("scissor cuts paper = computer win")
        computer_score +=1
    else:
        print("paper cover rock = you win") 
        user_score +=1

elif user_choice=="scissor":
    if comp_choice=="paper":
        print("scissor cuts paper = you win")
        user_score +=1
    else:
        print("rock smashes scissor = computer win")
        computer_score +=1
else: 
    print("Invalid input!No points given.")
    print(f"score->you :{user_score} | computer:{computer_score}")

print("Final result")
print(f"Final score-> you:{user_score} | computer:{computer_score}")

if user_score > computer_score:
    print("Congratulations!!!! You are the winner!")
elif computer_score > user_score:
    print("Computer is the winner!!!")
else:
    print("The game is tie!")    
            
