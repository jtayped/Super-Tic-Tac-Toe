
def checkWin(board):
    for col in board:
        if col[0] == col[1] == col[2] != ' ':
            return col[0]
    
    rows = []
    for i in range(len(board)):
        rows.append([])
        for col in board:
            rows[i].append(col[i])

    for row in rows:
        if row[0] == row[1] == row[2] != ' ':
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return board[2][0]
    
    return None


board = [
    ['o', ' ', 'o'],
    ['x', ' ', 'x'],
    ['o', 'o', 'o'],
]

print(checkWin(board))