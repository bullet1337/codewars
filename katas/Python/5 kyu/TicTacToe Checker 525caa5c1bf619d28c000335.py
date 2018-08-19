# https://www.codewars.com/kata/525caa5c1bf619d28c000335
def isSolved(board):
    empty = 0
    for i in range(len(board)):
        row = set(board[i])
        if len(row) == 1:
            x = row.pop()
            if x > 0:
                return x
            else:
                empty = -1
        elif 0 in row:
            empty = -1
    
    for i in range(len(board)):
        col = set(row[i] for row in board)
        if len(col) == 1:
            x = col.pop()
            if x > 0:
                return x
    
    diag = set(board[i][i] for i in range(len(board)))
    if len(diag) == 1:
        x = diag.pop()
        if x > 0:
            return x
        
    diag = set(board[i][len(board) - i - 1] for i in range(len(board)))
    if len(diag) == 1:
        x = diag.pop()
        if x > 0:
            return x
    
    return empty
        