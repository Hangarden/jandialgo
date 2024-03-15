import copy
from collections import deque
n = int(input())
map = []
for _ in range(n):
    x = list(input())
    map.append(x)
# print(map)

visited = [ ([False] * n)for _ in range(n) ]
# print(visited)
visited2 = copy.deepcopy(visited)
answer = 0
answer2 = 0


dxs, dys = [1,-1,0,0],[0,0,1,-1]
def bfs(i,j):
    visited[i][j] = True
    q = deque()
    color = map[i][j]
    q.append((i,j))

    while q:

        x, y = q.popleft()

        for k in range(4):
            nx = x + dxs[k]
            ny = y + dys[k]

            if 0<= nx < n and 0 <= ny < n and map[nx][ny] == color and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

    return 1


def bfs2(i,j):
    visited2[i][j] = True
    q = deque()
    q.append((i,j))
    if map[i][j] == "R" or map[i][j] == "G":
        color = ["R", "G"]
    else:
        color = [map[i][j]]
    while q:

        x, y = q.popleft()

        for k in range(4):
            nx = x + dxs[k]
            ny = y + dys[k]

            if 0<= nx < n and 0 <= ny < n and (map[nx][ny] in color) and not visited2[nx][ny]:
                q.append((nx, ny))
                visited2[nx][ny] = True

    return 1


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer += bfs(i,j)
        if not visited2[i][j]:
            answer2 += bfs2(i,j)

print(answer, answer2)