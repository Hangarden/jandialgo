n = int(input())

lst = list(map(int, input().split()))

max_val = -1001
curr = 0
for i in range(n):

    curr += lst[i]
    if curr > max_val:
        max_val = curr

    if curr <= 0:
        curr = 0

    # print(curr, max_val)

print(max_val)