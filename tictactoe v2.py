"""
this code version first checks the winning of ai in a row ,column,diagonal wise then place there
else checks for other players move and stops it 
otherthan it choose a random place to place the value
it is upgraded to make_2 function and detect and stops the make_2 of opposition
"""


def smart(mat,play) :
    opp = "X" if play == "O" else "O"
    
    # for checking each row
    player_count = 0
    oppose_count = 0  # counts the three symbols
    empty_count = 0
    right = None  # returns the right cell
    for i in range(3):
        for j in range(3) :
            if mat[i][j] == play :
                player_count += 1
            elif mat[i][j] == opp :
                oppose_count += 1
            else :
                empty_count += 1
                right = j       #  stores the col that we place our symbol
        
        if player_count == 2 and empty_count == 1 :
            return (i,right)
        # variables are started from 0 again
        player_count = 0
        oppose_count = 0  # counts the three symbols
        empty_count = 0
        right = None  # returns the right cell
            

    # checks the each column   
    player_count = 0
    oppose_count = 0  # counts the three symbols
    empty_count = 0
    right = None  # returns the right cell
    for i in range(3):
        for j in range(3) :
            if mat[j][i] == play :
                player_count += 1
            elif mat[j][i] == opp :
                oppose_count += 1
            else :
                empty_count += 1
                right = j       #  stores the col that we place our symbol
        if player_count == 2 and empty_count == 1 :
            return (right,i)
        
        # variables are started from 0 again
        player_count = 0
        oppose_count = 0  # counts the three symbols
        empty_count = 0
        right = None  # returns the right cell

    # for diagonal 1
    player_count = 0
    oppose_count = 0  # counts the three symbols
    empty_count = 0
    right = None  # returns the right cell    
    for i in range(3):
        if mat[i][i] == play :
                player_count += 1
        elif mat[i][i] == opp :
            oppose_count += 1
        else :
            empty_count += 1
            right = i      #  stores the col that we place our symbol
        if player_count == 2 and empty_count == 1 :
            return (right,right)
        
    # for diagonal 2
    player_count = 0
    oppose_count = 0  # counts the three symbols
    empty_count = 0
    right = None  # returns the right cell    
    for i in range(3):
        if mat[i][2-i] == play :
                player_count += 1
        elif mat[i][2-i] == opp :
            oppose_count += 1
        else :
            empty_count += 1
            right = i      #  stores the col that we place our symbol
        if player_count == 2 and empty_count == 1 :
            return (right,2-right)
        
    return (float('inf'),float('inf'))

def random_choice(mat):
    for i in range(3) :
        for j in range(3):
            if mat[i][j] == " ":
                return (i,j)
    return (float('inf'),float('inf'))


 
            
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
        last_choice = (row,col)   # not useful in this version
    else :  # AI moves
        row , col = smart(board , player)
        if (row,col) == (float('inf'),float('inf')) :
            opp_player = "X" if player == "O" else "O" # opp player stop proccess
            row,col = smart(board,opp_player)
        if (row,col) == (float('inf'),float('inf')) :
            row , col = random_choice(board)    # this gives random empty cell
        if (row,col) == (float('inf'),float('inf')) :
            print("something wrong happened")
            break

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
    