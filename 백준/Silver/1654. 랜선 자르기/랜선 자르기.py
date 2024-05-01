import sys

input = sys.stdin.readline
N, K =  map(int, input().split())

lst = []

for _ in range(N):
    lst.append(int(input()))
# print(lst)
min_val = 1
max_val = max(lst)

while min_val <= max_val:
    mid = (min_val + max_val) // 2

    cnt = 0
    # print(mid)
    for i in lst:
        cnt += (i // mid)
    # print(cnt)
    if cnt >= K:
        min_val = mid + 1
    else:
        max_val = mid - 1

print(max_val)