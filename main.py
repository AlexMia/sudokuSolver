import os

board = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
         [0, 6, 2, 0, 5, 0, 0, 9, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 6, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 8, 0, 0, 5, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 0],
         [0, 2, 0, 0, 1, 0, 7, 5, 0],
         [3, 8, 0, 0, 7, 0, 0, 4, 2]]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def printBoard():
    for x in range(len(board)):
        string = ''
        if x == 3 or x == 6:
            print('---------------------')
        for y in range(len(board[x])):
            if y == 3 or y == 6:
                string += '| '
            if not board[x][y]:
                string += '  '
            else:
                string += str(board[x][y]) + ' '
        print(string)

def findFirstNotEmpty():
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return x, y
    return -1, -1

def isValid(x, y, n):
    rowValid = all([n != board[x][j] for j in range(9)])
    if rowValid:
        colValid = all([n != board[i][y] for i in range(9)])
        if colValid:
            topX, topY = 3*(x//3), 3*(y//3)
            for i in range(topX, topX+3):
                for j in range(topY, topY+3):
                    if board[i][j] == n:
                        return False
            return True
    return False

def solve():
    x, y = findFirstNotEmpty()
    if x == -1:
        return True
    
    for n in range(1, 10):
        if isValid(x, y, n):
            board[x][y] = n
            if solve():
                return True
            board[x][y] = 0
    return False


clear()
printBoard()
solve()
print('\n'*3)
printBoard()