n = int(input())

DP = [1] * 10003
# print(DP)

for i in range(2,10002):
    DP[i] += DP[i-2]

for i in range(3,10003):
    DP[i] += DP[i-3]
lst= []
for _ in range(n):
    lst.append(int(input()))

for x in lst:
    print(DP[x])