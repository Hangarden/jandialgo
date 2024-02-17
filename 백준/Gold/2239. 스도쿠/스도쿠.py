def isValid(board, row, col, num):
    # 행, 열, 그리고 3x3 서브그리드에서 num의 유효성 검사
    for x in range(9):
        if board[row][x] == num: return False
        if board[x][col] == num: return False
        if board[3*(row//3) + x//3][3*(col//3) + x%3] == num: return False
    return True

def solveSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '0':  # 빈 칸 찾기
                for num in '123456789':
                    if isValid(board, i, j, num):
                        board[i][j] = num  # 시도
                        if solveSudoku(board):
                            return True  # 해결됨
                        board[i][j] = '0'  # 되돌리기
                return False  # 해결 불가
    return True  # 모든 빈 칸이 채워짐

# 스도쿠 보드 입력 받기
sdoku = [list(input()) for _ in range(9)]

if solveSudoku(sdoku):
    for row in sdoku:
        print(''.join(row))
else:
    print("No solution")
