"""
this version code intelligently checks the winning of opposite player and stops it .
but it stops according to opposition move [i,j] ( only checks the ith row and jth column and respective diagonals ) thats why not stop all times.
it not intelligently worked for himself. only stops the other wins as checking
if there are no win for opposite then it choose his move randomly
"""
def smart(mat,row,col,play) :
    if play == "X":
        play = "O"
    else :
        play = "X"
    n = len(mat)
    m = len(mat[0])
    play_count = 0
    empty = 0
    opp = 0
    right_column = None # when a row is winning then respective column value takes by it
    # for a row
    for j in range(3) :
        if mat[row][j] == play:
            play_count += 1
        elif mat[row][j] == " " :
            empty += 1
            right_column = j
        else:
            opp += 1
    if play_count == 2 and empty == 1 :
        return (row,right_column)
    
    # for column
    play_count = 0
    empty = 0
    opp = 0
    right_column = None
    for j in range(3) :
        if mat[j][col] == play:
            play_count += 1
        elif mat[j][col] == " " :
            empty += 1
            right_column = j
        else:
            opp += 1
    if play_count == 2 and empty == 1 :
        return (right_column,col)
    
    if col == row :
        # for diagonal 1
        play_count = 0
        empty = 0
        opp = 0
        right_column = None
        for j in range(3) :
            if mat[j][j] == play:
                play_count += 1
            elif mat[j][j] == " " :
                empty += 1
                right_column = j
            else:
                opp += 1
        if play_count == 2 and empty == 1 :
            return (right_column,right_column)
        
    if (col+row) == 2 :
        # diagonal 2 check
        play_count = 0
        empty = 0
        opp = 0
        right_column = None
        for j in range(3) :
            if mat[j][3-j-1] == play:
                play_count += 1
            elif mat[j][3-j-1] == " " :
                empty += 1
                right_column = j
            else:
                opp += 1
        if play_count == 2 and empty == 1 :
            return (right_column,3-right_column-1)
    # it been optimised in future 
    for i in range(3):
        for j in range(3):
            if mat[i][j] == " " :
                return (i,j)
            



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
    if player == "X" :
        row , col = list(map(int , input("enter the player " + player+ " choice").split()))
        last_choice = (row,col)
    else :
        row , col = smart(board , last_choice[0] , last_choice[1] , player)

    # actual placing at board , and checking winning proccess
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
    