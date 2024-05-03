from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)
lst = deque(list(range(1, n + 1)))
# print(lst)
cnt = 0

for num in nums:
    while True:
        if lst[0] == num:
            lst.popleft()
            break
        if lst.index(num) <= (len(lst)//2):
            lst.rotate(-1)
            cnt += 1
        else:
            lst.rotate(1)
            cnt += 1

print(cnt)