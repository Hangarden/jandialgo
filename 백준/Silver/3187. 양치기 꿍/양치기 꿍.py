from collections import deque

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
maps = []
wolf, sheep = 0, 0
for _ in range(n):
    maps.append(input())

dx, dy = [1,-1,0,0], [0,0,1,-1]
def bfs(x1,y1):
    # print(x1, y1, maps[x1][y1])
    global wolf, sheep
    q = deque()
    q.append((x1,y1))
    v, k = 0, 0
    if maps[x1][y1] == "k":
        k += 1
    else:
        v += 1



    while q:
        x, y = q.popleft()
        visited[x][y] = True


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and maps[nx][ny] != "#":
                if maps[nx][ny] == "k":
                    k += 1
                elif maps[nx][ny] == "v":
                    v += 1
                q.append((nx,ny))
                visited[nx][ny] = True
    # print(v, k)
    if v >= k:
        # print(v)
        wolf += v
    else:
        # print(k)
        sheep += k
    return




for i in range(n):
    for j in range(m):
        if not visited[i][j] and maps[i][j] != "#" and maps[i][j] != ".":
            bfs(i,j)

print(sheep, wolf)