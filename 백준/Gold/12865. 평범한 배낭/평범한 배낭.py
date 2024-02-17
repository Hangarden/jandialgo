n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# print(dp)
for i in range(1, n+1):
    weight, value = map(int, input().split())
    for w in range(1,k+1):
        if w >= weight:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
        else:
            dp[i][w] = dp[i-1][w]

print(max(dp[-1]))
