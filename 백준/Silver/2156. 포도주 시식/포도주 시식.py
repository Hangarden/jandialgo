n = int(input())
wines = [0] + [int(input()) for _ in range(n)]  # 포도주 양 입력 받기, 1부터 인덱싱하기 위해 앞에 0 추가
dp = [0] * (n+1)  # DP 테이블 초기화

# 초기 조건 설정
dp[1] = wines[1]
if n > 1:
    dp[2] = wines[1] + wines[2]

# DP를 이용한 최대 포도주 양 계산
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])

print(dp[n])
