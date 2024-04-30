from collections import deque

def bfs(x,y,n,m,maps):
    
    dxs,dys = [0,0,1,-1],[1,-1,0,0] # 동서남북
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0<= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    # print(n, m)
    bfs(0,0,n, m, maps)
    if maps[-1][-1] == 1:
        answer = -1
    else:
        answer = maps[-1][-1]
    return answer