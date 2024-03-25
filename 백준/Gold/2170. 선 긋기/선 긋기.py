import sys
input = sys.stdin.readline
n = int(input())

lines = []

for _ in range(n):
    lines.append(list(map(int, input().split())))

lines.sort()
# print(lines)
start, end = -1000000001, -1000000001
answer = 0
# print(start, end)
for x,y in lines:
    if x > end:
        answer += end - start
        start = x
        end = y

    elif start <= x  and y > end:
        end = y

answer += end - start

print(answer)

