
import sys

input = sys.stdin.readline
N,M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
# print(visited)
max_val = 0
# print(n,m)
# print(maps)

dx, dy = [1,-1,0,0],[0,0,1,-1]
def dfs(n, sm, tlst):
    global max_val
    if n == 4:
        max_val = max(max_val, sm)
        # print(lst)
        return

    for ci,cj in tlst:  # 도형의 모든위치에서 네방향
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 범위내 미방문이면 다음단계로
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0:
                v[ni][nj]=1
                dfs(n+1, sm+maps[ni][nj], tlst+[(ni,nj)])
                v[ni][nj]=0

for i in range(N):
    for j in range(M):  # 가능한 모든위치에서 dfs 탐색
        v[i][j]=1
        dfs(1, maps[i][j], [(i,j)])

print(max_val)