import sys
input = sys.stdin.readline
def valid(board, row, column, number):

    for x in range(9):
        if board[row][x] == number:
            return False
        if board[x][column] == number:
            return False
        if board[3 * (row//3) + x//3][3 * (column//3) + x%3] == number:
            return False
    return True


def sdoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for nums in range(1,10):
                    if valid(board, i, j, nums):
                        board[i][j] = nums
                        if sdoku(board):
                            return True
                        board[i][j] = 0
                return False

    return True


board = []

for i in range(9):
    board.append(list(map(int, input().split())))
# print(board)
sdoku(board)

for i in board:
    print(*i)