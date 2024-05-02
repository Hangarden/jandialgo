import sys

input = sys.stdin.readline

str1 = input().rstrip()
str1 = list(str1)
# print(str1)
n = int(input())
str2 = []
for _ in range(n):
    command = list(input().split())

    if command[0] == "L":
        if len(str1) >= 1:
            str2.append(str1.pop())
    elif command[0] == "D":
        if len(str2) >= 1:
            str1.append(str2.pop())
    elif command[0] == "B":
        if len(str1) >= 1:
            str1.pop()
    else:
        str1.append(command[1])

str1.extend(reversed(str2))
# print(str1)
print("".join(str1))