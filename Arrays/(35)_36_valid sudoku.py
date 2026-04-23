board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# validating rows
for i in range(9): # i is for rows, j is for columns
    seen = set()
    for j in range(9):
        if board[i][j] != '.':
            if board[i][j] in seen:
                print("False, sudoko is wrong")
            else:
                seen.add(board[i][j])
# validating columns
for i in range(9): # i is for columns, j is for rows
    seen = set()
    for j in range(9):
        if board[j][i] != '.':
            if board[j][i] in seen:
                print(False," sudoko is wrong")
            else:
                seen.add(board[j][i])
# validating 3*3 sub-boxes 
start  =[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)] 
# these are the starting points of each 3*3 sub-boxes, 
# we will iterate through each sub-box and check for duplicates
for x,y in start:
    seen = set()
    for i in range(x,x+3):
        for j in range(y,y+3):
            if board[i][j] !='.':
                if board[i][j] in seen:
                    print(False, "sudoko is wrong")
                else:
                    seen.add(board[i][j])
print(True,"sudoko is valid")

