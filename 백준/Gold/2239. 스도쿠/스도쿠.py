# 논리적인 아이디어

# 1. 0 -> 빈칸에 숫자들을 넣응면 된다
# 숫자는 아래와 같은 규칙을 지키며 넣으면 된다.
    # 1. 같은 행에 똑같은 숫자가 없으면 된다. [row][x] != num
    # 2. 같은 열에 똑같은 숫자가 없으면 된다. [x][column] != num
    # 3. 같은 구역에 똑같은 숫자가 없으면 된다.
        # 3-1. 같은 구역은 어떻게 산정하나?
            # 0,0 ~ 2,2
            # 3,3 ~ 5,5
            # 6,6 ~ 8,8
        # 3-2. 숫자가 2라면 구역은 [3*(row//3) + x//3 ] [ 3 * (col//3) + x%3 ] 와 같다
        # [row][x] != num
        # [x][column] != num
        # [3*(row//3) + x//3 ] [ 3 * (col//3) + x%3 ]
        # 를 만족하는 곳에 숫자를 쌓아간다. 만일 만족하는 구역이 없다면 False이다!
        # 만족하는 구역이 있다면 True!



# print(sdoku)

# 숫자를 넣을 수 있는지 확인하는 함수

board = []

for _ in range(9):
    board.append(list(map(int, input())))
def is_valid(board, row, column, number):

    for x in range(9):
        if board[row][x] == number:
            return False
        if board[x][column] == number:
            return False
        if board[3*(row//3) + x//3][3*(column//3) + x % 3] == number:
            return False

    return True
# 스토쿠 숫자 놓기
def sdoku(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if sdoku(board):
                            return True
                        board[i][j] = 0
                return False

    return True


if sdoku(board):
    for row in board:
        for i in row:
            print(i, end="")
        print()
else:
    print("No answer")

