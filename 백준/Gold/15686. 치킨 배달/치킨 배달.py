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
# print(chicken, home)

chickens = list(combinations(chicken,M))
# print(len(chicken))
answer = 0

# for i in home:
#     print(i)
max_val = float('inf')
# for x in chicken:
#     for y in home:
#         print(x,y)
#

# for chi in chicken:
#     print(chi)
#     for x in chi:
#         print(x)
#         for y in home:
#             print(y)

# print(len(chicken))
# print(home)
total_min_val = float('inf')

# for home in homes:
#     answer = 0
#     for chi in chicken:
#         min_val = float('inf')
#         for x in chi:
#             min_val = min(min_val, abs[h])
for chicken in chickens:
    answer = 0
    for home in homes:
        min_val = float('inf')
        for x in chicken:
            min_val = min(min_val, abs(home[0] - x[0]) + abs(home[1] - x[1]))
        answer += min_val
    # print(answer)
    total_min_val = min(answer, total_min_val)
#
print(total_min_val)


# total_min_val = float('inf')
# for chi in chicken:
#     answer =0
#     for x in chi: # 10
#         min_val = float('inf')
#         for y in home: # 6
#             min_val = min(min_val, abs(x[0] - y[0]) + abs(x[1] - y[1]))
#         answer += min_val
#         print(answer)
#     total_min_val = min(answer, total_min_val)
# print(total_min_val)
