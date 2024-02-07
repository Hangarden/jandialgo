import sys

input = sys.stdin.readline

# 행렬의 크기
n = int(input())

# 1.꼭 명시적으로 함수의 return을 만나지 않아도 2.더 이상 실행할 코드가 없다면 종료 됌
# 2의 경우 실행되었던 곳으로 돌아감 -> 백트래킹의 원리
def dfs(x):
    # 가능한 경우의 수를 놓는 경우
    global answer
    # n행까지 왔으면 n-1까지 말을 다 놓은 것임으로 완료해야한다
    if x == n:
        answer += 1
        return
    for i in range(n):
        # 열, 대각선(/), 대각선 \ 을 동시에 만족하는 인덱스 말을 놓지 않았다면
        # / -> x,y 좌표의 합이 같은 곳, \ -> x-y의 차이가 같은 곳
        # 만족하면 계속해서 말을 놓고 아니라면 다음 행으로 가는 거 아닌가
        if v1[i] == v2[x + i] == v3[x - i] == 0:
            v1[i] = v2[x + i] = v3[x - i] = 1
            dfs(x + 1)
            v1[i] = v2[x + i] = v3[x - i] = 0


v1, v2, v3 = [[0] * (n * 2) for _ in range(3)]
answer = 0
dfs(0)
print(answer)


