import math
import sys

input = sys.stdin.readline
N, C = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(int(input()))

lst.sort()

end = lst[-1] - lst[0]
start = 1

while start <= end:
    cnt = 1
    curr = lst[0]
    mid = (start + end) // 2

    for i in lst[1:]:
        if i - curr >= mid:
            curr = i
            cnt += 1

    if cnt >= C: # 설치개수가 많다면 간격을 넓혀야 함
        start = mid + 1 # 더 넓은 간격으로 시도
    elif cnt < C: # 설치개수가 목표개수보다 작다면 간격을 좁혀야 함
        end = mid - 1

print(end)