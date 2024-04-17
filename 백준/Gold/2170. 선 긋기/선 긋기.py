import sys

input = sys.stdin.readline

lst = []
n = int(input())
for _ in range(n):
    lst.append(tuple(map(int, input().split())))

lst.sort()
# print(lst)

max_val, min_val = -10000000001,-10000000001
answer = 0
for x, y in lst:
    # print(x, y)
    if max_val < x:
        answer += max_val - min_val
        min_val = x
        max_val = y
    elif max_val < y:
        max_val = y
        continue

answer += max_val - min_val

print(answer)