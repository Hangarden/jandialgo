from itertools import *
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

maps = [list(map(int,input().split())) for _ in range(N)]


chicken = []
homes = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            chicken.append((i,j))
        if maps[i][j] == 1:
            homes.append((i,j))
            
chickens = list(combinations(chicken,M))
answer = 0
max_val = float('inf')
total_min_val = float('inf')

for chicken in chickens:
    answer = 0
    for home in homes:
        min_val = float('inf')
        for x in chicken:
            min_val = min(min_val, abs(home[0] - x[0]) + abs(home[1] - x[1]))
        answer += min_val
    # print(answer)
    total_min_val = min(answer, total_min_val)

print(total_min_val)