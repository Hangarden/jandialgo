import sys

input = sys.stdin.readline
n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

# print(lst)

lst.sort()

for x in lst:
    print(x)