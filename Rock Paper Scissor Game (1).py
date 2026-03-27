import random 

item_list = ["rock","paper","scissor"]


p1 = input("Player 1 move (rock, paper, scissor) = ").lower()
p2 = input("Player 2 move (rock, paper, scissor) = ").lower()
p3 = input("Player 3 move (rock, paper, scissor) = ").lower()


if p1 not in item_list:
    print("Player 1 invalid → OUT ")
    p1 = None

if p2 not in item_list:
    print("Player 2 invalid → OUT ")
    p2 = None

if p3 not in item_list:
    print("Player 3 invalid → OUT ")
    p3 = None



valid = []
names = []

if p1 != None:
    valid.append(p1)
    names.append("Player 1")

if p2 != None:
    valid.append(p2)
    names.append("Player 2")

if p3 != None:
    valid.append(p3)
    names.append("Player 3")



if len(valid) == 0:
    print("No valid players ")

elif len(valid) == 1:
    print(f"{names[0]} is the winner ")

elif len(valid) == 2:
    print(f"{names[0]} = {valid[0]}")
    print(f"{names[1]} = {valid[1]}")

    if valid[0] == valid[1]:
        print("Match Tie ")

    elif valid[0] == "rock":
        if valid[1] == "paper":
            print(f"{names[1]} wins ")
        else:
            print(f"{names[0]} wins ")

    elif valid[0] == "paper":
        if valid[1] == "scissor":
            print(f"{names[1]} wins ")
        else:
            print(f"{names[0]} wins ")

    elif valid[0] == "scissor":
        if valid[1] == "rock":
            print(f"{names[1]} wins ")
        else:
            print(f"{names[0]} wins ")


elif len(valid) == 3:
    print(f"Player 1 = {p1}")
    print(f"Player 2 = {p2}")
    print(f"Player 3 = {p3}")

   
    if p1 == p2 and p2 == p3:
        print("All same → Tie ")

   
    elif (p1 != p2) and (p2 != p3) and (p1 != p3):
        print("All different → Tie ")

    else:
        
        if ("rock" in valid) and ("scissor" in valid):
            win = "rock"
        elif ("paper" in valid) and ("rock" in valid):
            win = "paper"
        else:
            win = "scissor"

       
        if p1 == win:
            print("Player 1 wins ")
        if p2 == win:
            print("Player 2 wins ")
        if p3 == win:
            print("Player 3 wins ")
