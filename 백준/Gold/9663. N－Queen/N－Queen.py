import sys

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())


# rows = [0] * N
# columns = [0] * N
# line1 = [0] * (2 * N)
# line2 = [0] * (2 * N)
columns, line1, line2 = [[0] * (N * 2 -1) for _ in range(3)]
# print(line2)
answer = 0
def n_queen(depth):
    global answer
    if depth == N:
        answer += 1
        return
    for i in range(N):
        if columns[i] == line1[depth + i] == line2[depth - i] == 0:
            columns[i] = line1[depth + i] = line2[depth - i] = 1
            n_queen(depth + 1)
            columns[i] = line1[depth + i] = line2[depth - i] = 0

    return

n_queen(0)
print(answer)

# v1, v2, v3 = [[0] * (N * 2 -1) for _ in range(3)]
# print(v1,v2,v3)