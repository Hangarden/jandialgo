import sys
import heapq
# 간 레벨 올려주기는 약간의 훼이크다
input = sys.stdin.readline
# 맥주들의 만족도 총합을 더해도 M보다 작다면 만들 수 없는 조합이다. -1

# 축제 기간(N <= 20만), 만족도(M <=무한대), 맥주 종류(K<= 200000)

N, M, K = map(int, input().split())

happy = []
for _ in range(K):
    # 만족도 도수
    a, b = map(int, input().split())
    happy.append((a,b))

beers = sorted(happy, key= lambda x:(x[1],x[0]))

n = 0
drinks = []
happy = 0
for beer in beers:
    # 행복도가 낮은 순 같다면 도수가 낮은 것부터 먼저들어옴

    heapq.heappush(drinks, beer[0])
    # print(drinks)
    happy += beer[0]
    # print(happy)


    if len(drinks) >= N:
        if happy >= M:
            print(beer[1])
            break
        else:
            happy -= heapq.heappop(drinks)
else:
    print(-1)