import random
min = 0
max = 100
player2_number = -1
count = 0
change = 0

while True:
    player1_number = int(input("Player 1: Enter a number between 0 and 100: "))
    if  100 >= player1_number >= 0:
        break
    else:
        print(f"You can enter a number only between {min} and {max}. Try again.")
        
while not player2_number == player1_number:
    while True:
        player2_number = int(input(f"Player 2: Guess a number between {min} and {max}: "))
        if  max >= player2_number >= min:
            break
        else:
            print(f"You can enter a number only between {min} and {max}. Try again.")
    count += 1
    if player2_number != player1_number:
        change = 0
    while change == 0:
        print("-Player 2's guess is",player2_number)
        if player2_number != player1_number:
            changer = str(input("Player 1: higher or lower? "))
            if changer == "higher":
                min = player2_number + 1
                change = 1
            elif changer == "lower":
                max = player2_number - 1
                change = 1
    if player2_number == player1_number:
        print("-Player 2's guess is",player2_number)
        print("victory!")

print("number of tries: ", count)