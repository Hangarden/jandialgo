lst = [1, 2, 4, 8, 16, 32, 64]

DP = [9999] * 66
k = int(input())
# print(DP)

DP[1] = 1

for i in range(2, 65):
    for x in lst:
        if i - x >= 0:
            if i-x == 0:
                DP[i] = 1
            else:
                DP[i] = min(DP[i], DP[i-x] + 1)
# print(DP)
print(DP[k])