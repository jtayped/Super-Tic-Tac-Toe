import pygame

WIDTH, HEIGHT = 720, 720
FPS = 60

def checkWin(board):
    for col in board:
        if col[0] == col[1] == col[2] and col[0] != ' ':
            return col[0]
    
    rows = []
    for i in range(len(board)):
        rows.append([])
        for col in board:
            rows[i].append(col[i])

    for row in rows:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' ':
        return board[2][0]
    
    return None