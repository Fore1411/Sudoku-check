


def main():

    board = [
    [3,2,8,9,7,4,1,6,5],
    [5,1,9,3,6,2,4,8,7],
    [4,6,7,8,5,1,2,9,3],
    [7,8,4,1,3,5,6,2,9],
    [9,5,2,7,8,6,3,1,4],
    [6,3,1,2,4,9,7,5,8],
    [8,9,6,4,2,7,5,3,1],
    [1,7,5,6,9,3,8,4,2],
    [2,4,3,5,1,8,9,7,6]
    ]

    print(check_board(board))

    

def check_board(board):
    #function will take in a board and would return a true false on whether or not it is a valid board
    #a board is a list of more lists of numbers 

    #check rows
    for row in board:
        if 1 not in row:
            return False
        elif 2 not in row:
            return False
        elif 3 not in row:
            return False
        elif 4 not in row:
            return False
        elif 5 not in row:
            return False
        elif 6 not in row:
            return False
        elif 7 not in row:
            return False
        elif 8 not in row:
            return False
        elif 9 not in row:
            return False
    #check columns 
    for i in range(8):
        column=[]
        column.append(board[0][i])
        column.append(board[1][i]) 
        column.append(board[2][i]) 
        column.append(board[3][i]) 
        column.append(board[4][i]) 
        column.append(board[5][i]) 
        column.append(board[6][i]) 
        column.append(board[7][i]) 
        column.append(board[8][i])  
        print(column)
        if 1 not in column:
            return False
        elif 2 not in column:
            return False
        elif 3 not in column:
            return False
        elif 4 not in column:
            return False
        elif 5 not in column:
            return False
        elif 6 not in column:
            return False
        elif 7 not in column:
            return False
        elif 8 not in column:
            return False
        elif 9 not in column:
            return False
       
    #chech grids 
    for x in range(2):
        for y in range(2):
            group=[]
            group.append(board[x*3][y*3])
            group.append(board[x*3][y*3+1])
            group.append(board[x*3][y*3+2])
            group.append(board[x*3+1][y*3])
            group.append(board[x*3+1][y*3+1])
            group.append(board[x*3+1][y*3+2])
            group.append(board[x*3+2][y*3])
            group.append(board[x*3+2][y*3+1])
            group.append(board[x*3+2][y*3+2])
            print(group)
            if 1 not in group:
                return False
            elif 2 not in group:
                return False
            elif 3 not in group:
                return False
            elif 4 not in group:
                return False
            elif 5 not in group:
                return False
            elif 6 not in group:
                return False
            elif 7 not in group:
                return False
            elif 8 not in group:
                return False
            elif 9 not in group:
                return False    

    return True




    
              

if __name__=="__main__":
    main()    
