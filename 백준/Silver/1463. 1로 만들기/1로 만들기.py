from collections import deque
n = int(input())
q = deque()
q.append(1)
DP = [float('inf')] * 1000003
DP[1] = 0
while True:
    x = q.popleft()

    if x == n:
        print(DP[n])
        break

    a = x + 1
    b = x * 2
    c = x * 3
    if a <= 1000000 and DP[a] > DP[x] + 1:
        DP[a] = DP[x] + 1
        q.append(a)
    if b <= 1000000 and DP[b] > DP[x] + 1:
        DP[b] = DP[x] + 1
        q.append(b)
    if c <= 1000000 and DP[c] > DP[x] + 1:
        DP[c] = DP[x] + 1
        q.append(c)