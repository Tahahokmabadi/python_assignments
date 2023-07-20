import pyfiglet
import random

print(pyfiglet.figlet_format("Rock Paper Scissors!"))

print("1-player vs computer\n2-player vs player")

while True:
    players = int(input("Your choice(1, 2): "))
    if players == 1:
        break
    elif players == 2:
        break

while True:
    rounds = int(input("enter number of rounds(1, 3 ,5): "))
    if rounds == 1:
        break
    elif rounds == 3:
        break
    elif rounds == 5:
        break
p1s = 0
p2s = 0
while True:
     if p1s == rounds:
        break
     elif p2s == rounds:
        break
     if players == 1:
            print("1-Rock\n2-Paper\n3-Scissors")
            choice1 = int(input("Your choice(1, 2, 3): "))
            choices = ["1", "2", "3"] 
            choice2 = random.choice(choices)
            if choice1 == choice2:
                print("tie!")
            elif choice1 == 1:
                if choice2 == 2:
                    print("camputer wins!")
                    p2s += 1
                else :
                    print("player 1 wins!")
                    p1s += 1
            elif choice1 == 2:
                if choice2 == 1:
                    print("player 1 wins!")
                    p1s += 1
                else :
                    print("camputer wins!")
                    p2s += 1
            elif choice1 == 3:
                if choice2 == 1:
                    print("camputer wins!")
                    p2s += 1
                else :
                    print("player 1 wins!")
                    p1s += 1
     elif players == 2:
        print("1-Rock\n2-Paper\n3-Scissors")
        choice1 = int(input("Your choice(1, 2, 3): "))
        print("1-Rock\n2-Paper\n3-Scissors")
        choice2 = int(input("Your choice(1, 2, 3): "))
        if choice1 == choice2:
            print("tie!")
        elif choice1 == 1:
            if choice2 == 2:
                print("player 2 wins!")
                p2s += 1
            else :
                print("player 1 wins!")
                p1s += 1
        elif choice1 == 2:
            if choice2 == 1:
                print("player 1 wins!")
                p1s += 1
            else :
                print("player 2 wins!")
                p2s += 1
        elif choice1 == 3:
            if choice2 == 1:
                print("player 2 wins!")
                p2s += 1
            else :
                print("player 1 wins!")
                p1s += 1
if p1s == rounds:
    print(pyfiglet.figlet_format("Player 1 is the WINNER!"))
else:
    if players == 2:
        print(pyfiglet.figlet_format("Player 2 is the WINNER!"))
    else:
        print(pyfiglet.figlet_format("Camputer is the WINNER!"))