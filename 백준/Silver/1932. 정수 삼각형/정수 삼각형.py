import sys
input = sys.stdin.readline
n = int(input())
d = [0]*n
for w in range(n):
    d[w] = list(map(int, sys.stdin.readline().split()))
# print(len(d[2]))


for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i-1][0] + d[i][j]
        elif j == len(d[i]) - 1:
            d[i][j] = d[i-1][j-1] + d[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + d[i][j]

print(max(d[-1]))
