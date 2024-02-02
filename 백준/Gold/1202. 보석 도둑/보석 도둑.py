import sys

import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
jewerly = []

for _ in range(n):
    x, y = map(int, input().split())
    jewerly.append([x,y])

bags = []

for _ in range(k):
    bags.append(int(input()))

jewerly.sort(key = lambda x : x[0] )
# print(jewerly)
bags.sort()
# print(bags)

temp = []
result = 0
for bags_weight in  bags:

    while jewerly and jewerly[0][0] <= bags_weight:
        heapq.heappush(temp, -jewerly[0][1])
        heapq.heappop(jewerly)
    if temp:
        result -= heapq.heappop(temp)
print(result)