from itertools import permutations
n = int(input())

nums = list(map(int, input().split()))

lists = list(permutations(nums))
# print(a)
max_val = 0
def cal(lst):
    diff = 0
    for i in range(n-1):
        diff += abs(lst[i] - lst[i+1])
    return diff
for x in lists:
    max_val = max(max_val, cal(x))

print(max_val)