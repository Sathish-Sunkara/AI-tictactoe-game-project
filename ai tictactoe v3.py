"""
this code version first checks the winning of ai in a row ,column,diagonal wise then place there
else checks for other players move and stops it 
otherthan it choose a random place to place the value
in this particular version (v3) the random choice function was upgraded of previous version
it checks the empty cells and claculates scores of each empty cell based on possibility of winnings in its row ,column and diagonals to be win in the future
it checks only there is make_2 in next move then place there the choice ,or it stops the the others make_2 cell 
thats why it is not store the all scores of empty cells in a score table .

"""
def best_choice(score_table) : # return best (i,j) 
    pass

def score1(mat,row,col,player,oppo):  # assign scores to each cell individually. 

    score = 0

    #score for a row
    player_count = 0
    oppo_count = 0
    empty_count = 0
    for i in range(3):
        if mat[row][i] == player :
            player_count += 1
        if mat[row][i] == oppo :
            oppo_count += 1
        if mat[row][i] == " " :
            empty_count += 1
        # conditions for scoring
        if player_count==1 and empty_count==2 :
            score += 4
        if empty_count==3 :
            score += 1
        if oppo_count==1 and empty_count==2 :
            score += 0   # these are not be winnings in future
        if oppo_count==1 and player_count==1 and empty_count==1 :
            score += 0

    # score for a column
    player_count = 0
    oppo_count = 0
    empty_count = 0
    for i in range(3):
        if mat[i][col] == player :
            player_count += 1
        if mat[i][col] == oppo :
            oppo_count += 1
        if mat[i][col] == " " :
            empty_count += 1
        # conditions for scoring
        if player_count==1 and empty_count==2 :
            score += 4
        if empty_count==3 :
            score += 1
        if oppo_count==1 and empty_count==2 :
            score += 0   # these are not be winnings in future
        if oppo_count==1 and player_count==1 and empty_count==1 :
            score += 0

    # for diagonal 1
    if row == col :
        player_count = 0
        oppo_count = 0
        empty_count = 0
        for i in range(3):
            if mat[i][i] == player :
                player_count += 1
            if mat[i][i] == oppo :
                oppo_count += 1
            if mat[i][i] == " " :
                empty_count += 1
            # conditions for scoring
            if player_count==1 and empty_count==2 :
                score += 4
            if empty_count==3 :
                score += 1
            if oppo_count==1 and empty_count==2 :
                score += 0   # these are not be winnings in future
            if oppo_count==1 and player_count==1 and empty_count==1 :
                score += 0

    # for diagonal 2
    if row == 2-col :
        player_count = 0
        oppo_count = 0
        empty_count = 0
        for i in range(3):
            if mat[i][2-i] == player :
                player_count += 1
            if mat[i][2-i] == oppo :
                oppo_count += 1
            if mat[i][2-i] == " " :
                empty_count += 1
            # conditions for scoring
            if player_count==1 and empty_count==2 :
                score += 4
            if empty_count==3 :
                score += 1
            if oppo_count==1 and empty_count==2 :
                score += 0   # these are not be winnings in future
            if oppo_count==1 and player_count==1 and empty_count==1 :
                score += 0
    return score




def make_2(mat,player) :              # scoring all empty cells and check if there is a make_2 cell

    oppo = "X" if player == "O" else "O"
    score = 0                         # this gets the score of a cell
    (row,col) = (float('inf') , float('inf'))

    # detect and validate empty cells
    for i in range(3):
        for j in range(3) :
            if mat[i][j] == " ":
                score = score1(mat,i,j,player,oppo)
                if score >= 8 :
                    (row,col) = (i,j)
                    #break

    return (row,col)
    


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
            row , col = make_2(board,player)    # intelligent move of player
        
        if (row,col) == (float('inf'),float('inf')) :
            opp = "X" if player=="O" else "O"
            row , col = make_2(board,opp)    # intelligent move of opposite player so we stpp here that move

        if (row,col) == (float('inf'),float('inf')) :
            (row,col) = random_choice(board)

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
    