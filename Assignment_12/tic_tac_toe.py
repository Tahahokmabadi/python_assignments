p1_char = input("type player 1 character: ")
p2_char = input("type player 2 character: ")

while True:
    if (p1_char == "-") or (p1_char == p2_char):
        print("player 1's character can't be this.")
        p2_char = input("type player 1 charcter: ")
    else:
          break
    
while True:
    if (p2_char == p1_char) or (p2_char == "-"):
        print("player 2's character can't be this.")
        p2_char = input("type player 2 character: ")
    else:
        break

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

def print_board(board):
    for i in range(3):
        print()
        for j in range(3):
           print(board[i][j], end= " ")
    print()

def vict(board):
    if ((board[0][0]) and (board[0][1]) and board[0][2]) == p1_char:
        winner = "1"
    elif ((board[1][0]) and (board[1][1]) and board[1][2]) == p1_char:
            winner = "1"
    elif ((board[2][0]) and (board[2][1]) and board[2][2]) == p1_char:
            winner = "1"
    elif ((board[0][0]) and (board[1][0]) and board[2][0]) == p1_char:
            winner = "1"
    elif ((board[0][1]) and (board[1][1]) and board[2][1]) == p1_char:
            winner = "1"
    elif ((board[0][2]) and (board[1][2]) and board[2][2]) == p1_char:
            winner = "1"
    elif ((board[0][0]) and (board[1][1]) and board[2][2]) == p1_char:
            winner = "1"
    elif ((board[0][2]) and (board[1][1]) and board[2][2]) == p1_char:
            winner = "1"
    elif ((board[0][0]) and (board[0][1]) and board[0][2]) == p2_char:
            winner = "2"
    elif ((board[1][0]) and (board[1][1]) and board[1][2]) == p2_char:
            winner = "2"
    elif ((board[2][0]) and (board[2][1]) and board[2][2]) == p2_char:
            winner = "2"
    elif ((board[0][0]) and (board[1][0]) and board[2][0]) == p2_char:
            winner = "2"
    elif ((board[0][1]) and (board[1][1]) and board[2][1]) == p2_char:
            winner = "2"
    elif ((board[0][2]) and (board[1][2]) and board[2][2]) == p2_char:
            winner = "2"
    elif ((board[0][0]) and (board[1][1]) and board[2][2]) == p2_char:
            winner = "2"
    elif ((board[0][2]) and (board[1][1]) and board[2][2]) == p2_char:
            winner = "2"
    elif ((board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2]) != "-"):
          winner = "3"
    else:
          winner = 0
    return winner
print_board(board)

player1_s = int(-1)
player1_r = int(-1)
player2_s = int(-1)
player2_r = int(-1)

while True:
    while True:
        while not (0 <= player1_s < 3):
            player1_s = (int(input("sotoon player 1(1, 2, 3): "))) -1
        while not (0 <= player1_r < 3):
            player1_r = (int(input("radif player 1(1, 2, 3): "))) -1
        if board[player1_s][player1_r] != "-":
            player1_s = -1
            player1_r = -1
        else:
            break

    board[player1_s][player1_r] = p1_char
    
    print_board(board)

    victory = vict(board)
    if (victory == "1") or (victory == "2") or (victory == "3"):
          break
    while True:
        while not (0 <= player2_s < 3):
            player2_s = (int(input("sotoon player 2(1, 2, 3): "))) -1
        while not (0 <= player2_r < 3):
            player2_r = (int(input("radif player 2(1, 2, 3): "))) -1
        if board[player2_s][player2_r] != "-":
                player2_s = -1
                player2_r = -1
        else:
            break
    board[player2_s][player2_r] = p2_char

    print_board(board)

    victory = vict(board)
    if (victory == "1") or (victory == "2") or (victory == "3"):
          break

if victory == "1":
      print("Player one won!")
elif victory == "2":
      print("Player two won!")
elif victory == "3":
      print("Draw!")