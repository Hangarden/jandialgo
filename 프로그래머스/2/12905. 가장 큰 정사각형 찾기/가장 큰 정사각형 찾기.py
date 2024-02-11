def solution(board):
    answer = 1234
    n = len(board)
    m = len(board[0])
    # print(n,m)
    DP = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    
    for i in range(m):
        if board[0][i] >= 1:
            DP[0][i] = 1
            
    for j in range(n):
        if board[j][0] >= 1:
            DP[j][0] = 1
    # print(DP)
    max_val = -1
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] >= 1:
                # print(i,j)
                if DP[i-1][j] >=1 and DP[i][j-1] >=1 and DP[i-1][j-1] >=1:
                    # print(i,j)
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
                    max_val = max(max_val, DP[i][j])
                else:
                    DP[i][j] = 1
    if count == n*m:
        answer = 0
    else:
        answer = max_val**2
    return answer