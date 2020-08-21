def DisplayBoard(board):
    t=0
    for i in range(4):
        print("+-------+-------+-------+")
        if i==3:
            break
        for j in range(3):
            if j==1:
                print("|  ", board[t], "  |  ", board[t+1], "  |  ", board[t+2], "  |")
                t += 3
            else:
                print("|       |       |       |")
            
        
def DrawMove(board):
    global sign
    sign = "X"
    for m in range(9):
        if (board[m] != "X") and (board[m] != "O"):
            board[m] = "X"
            break        
    MakeListOfFreeFields(board)


def VictoryFor(board, sign):

    if (board[0]=="X" and board[1]=="X" and board[2]=="X") or \
    (board[3]=="X" and board[4]=="X" and board[5]=="X") or \
    (board[6]=="X" and board[7]=="X" and board[8]=="X") or \
    (board[0]=="X" and board[3]=="X" and board[6]=="X") or \
    (board[1]=="X" and board[4]=="X" and board[7]=="X") or \
    (board[2]=="X" and board[5]=="X" and board[8]=="X") or \
    (board[0]=="X" and board[4]=="X" and board[8]=="X") or \
    (board[2]=="X" and board[4]=="X" and board[6]=="X") :
        print ("Oops! The system won the game!")
        return
    elif (board[0]=="O" and board[1]=="O" and board[2]=="O") or \
    (board[3]=="O" and board[4]=="O" and board[5]=="O") or \
    (board[6]=="O" and board[7]=="O" and board[8]=="O") or \
    (board[0]=="O" and board[3]=="O" and board[6]=="O") or \
    (board[1]=="O" and board[4]=="O" and board[7]=="O") or \
    (board[2]=="O" and board[5]=="O" and board[8]=="O") or \
    (board[0]=="O" and board[4]=="O" and board[8]=="O") or \
    (board[2]=="O" and board[4]=="O" and board[6]=="O") :
        print ("Wow! You won the game!")
        return
    elif all(isinstance(k, str) for k in board):
        print("The game is a TIE")
        return
    elif sign == "O":
        DrawMove(board)
    else:
        EnterMove(board)
        

def MakeListOfFreeFields(board):
    global sign
    DisplayBoard(board)
    VictoryFor(board, sign)

def EnterMove(board):

    n = int(input("Enter your move: "))
    if n<=0 or n>=10 or n not in board:
        print("Invalid input.")
        EnterMove(board)
    else:
        board[n-1] = "O"
    global sign
    sign = "O"
    MakeListOfFreeFields(board)

print("Please select a number 1~9 to place your sign [O]")
freeFields = [1, 2, 3, 4, "X", 6, 7, 8, 9]
sign = ""
DisplayBoard(freeFields)
EnterMove(freeFields)
