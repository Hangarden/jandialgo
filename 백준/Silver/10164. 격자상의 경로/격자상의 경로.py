N, M, K = map(int, input().split())

dp =  [1] * 35

for i in range(1, 34):
    dp[i] = dp[i-1] * i

# print(dp)
if K != 0:
    x = ((K-1) // M) # 1 -> 0
    y = ((K-1) % M) # 1 -> 0
    a = dp[x+y] / ( dp[x] * dp[y] ) # 1

    after_x = N - 1 - x # 0
    after_y = M - 1 - y # 0
    b = dp[after_x + after_y] / (dp[after_x] * dp[after_y])

    print(int(a*b))
else:
    a = dp[N-1]
    b = dp[M-1]
    c = dp[N+M-2]
    print(int(c / (a * b)))



