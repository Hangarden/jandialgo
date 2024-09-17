# 아이디어
# 백 트레킹을 통해 모든 경우의 수를 탐색한다.
# 시간복잡도
# 백 트레킹의 경우 재귀함수를 사용한다. 범위가 8~10 사이라면 백트레킹일 확률이 높다
# 자료구조
# 방문처리 리스트
# 출력을 위한 LIST
import sys


input = sys.stdin.readline
n, m = map(int, input().split())
visited = [False] * (n+1)
rs = []
def recur(num):

    if num == m:
        print(' '.join(map(str, rs)))
    for i in range(1, n+1):
        if visited[i] == False:
            rs.append(i)
            visited[i] = True
            recur(num+1)
            visited[i] = False
            rs.pop()

recur(0)

