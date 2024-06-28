def printboard(board) :
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            print(" | "+board[i][j] , end = "")
        print()

def haswon(board ,r,c,play) :
    for i in range(3):
        if board[r][i] != play :
            break    
    else :
        return True

    for i in range(3):
        if board[i][c] != play :
            break    
    else :
        return True

    if board[1][1] == play and board[0][0] == play and board[2][2] == play :
        return True
    if board[0][2] == play and board[1][1] == play and board[2][0] == play :
        return True
    return False
            


# creating board
board = [[" "]*3 for i in range(3)]
gameover = False
player = 'X'
count = 0  # this varible reaches 9  then board is filled . but while loop not terminates using this variable we terminates the while loop

while not gameover:
    printboard(board)
    # placing your choice
    row , col = list(map(int , input("enter the player " + player+ " choice").split()))

    if (row >= 0 and row <= 2) and (col >= 0 and col <= 2) and (board[row][col] == " ") :
        board[row][col] = player
        count += 1

        if haswon(board , row , col ,player) :
            printboard(board)
            print("the playes " + player + " won the game")
            gameover = True
            break

        elif count == 9 :
            printboard(board)
            print(" no one won the game ")
             # below code for restart the game again to start fresh board but there is a bug to fix 
            """print("can you start again (y / n")
            input = input()
            if input == "y" :
                # start all values freshly
                count = 0
                board = [[" "]*3 for i in range(3)]
                player = "X"
            else:
                print(" thank you visit again !!!") 
                break """
            
            gameover = True
            break

        else :
            if player == "X" :
                player = "O"
            else :
                player = "X"
    
    else :
        print("invalid move")
    