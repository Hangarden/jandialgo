from collections import deque
import copy

# def find_lever(count_maps, S, visited, origin_maps):
#     global answer
#     q = deque()
#     q.append(S)
#     visited[S[0]][S[1]] = True
    
#     dxs, dys = [1,-1,0,0], [0,0,1,-1]
    
#     while q:
#         x, y = q.popleft()
        
#         for i in range(4):
#             nx = x + dxs[i]
#             ny = y + dys[i]
        
#             if 0<= nx < len(count_maps) and 0<= ny < len(count_maps[0]) and not visited[nx][ny] and origin_maps[nx][ny] != "X" :
#                 q.append((nx,ny))
#                 visited[nx][ny] = True
#                 count_maps[nx][ny] = count_maps[x][y] + 1
#     return count_maps

# def find_exit(count_maps, L, visited, origin_maps):
#     global answer
#     q = deque()
#     q.append(L)
#     visited[L[0]][L[1]] = True    
    
#     dxs, dys = [1,-1,0,0], [0,0,1,-1]
    
#     while q:
#         x, y = q.popleft()
        
#         for i in range(4):
#             nx = x + dxs[i]
#             ny = y + dys[i]
        
#             if 0<= nx < len(count_maps) and 0<= ny < len(count_maps[0]) and not visited[nx][ny] and origin_maps[nx][ny] != "X" :
#                 q.append((nx,ny))
#                 visited[nx][ny] = True
#                 count_maps[nx][ny] = count_maps[x][y] + 1

def valid(x,y, maps):
    
    return 0<= x < len(maps) and 0 <= y < len(maps[0])

def bfs(x, y, lever, count, visited, q):
    if not visited[x][y][lever]:
        visited[x][y][lever] = True
        q.append((x, y, lever, count+1))
        
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[ [False, False] for _ in range(m)] for _ in range(n)  ]
    lever_map = [[0] * m for _ in range(n)] 
    q = deque()
    # print(visited)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "L":
                L = [i,j]
            elif maps[i][j] == "S":
                q.append((i, j, 0, 0))
            elif maps[i][j] == "E":
                end_x = i
                end_y = j
    print(maps)
    # print(L, S, E)
    
    dxs, dys = [1,-1,0,0], [0,0,1,-1]
    while q:
        x,y,l,count = q.popleft()
        
        if x == end_x and y == end_y and l == 1:
            return count
        
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            
            if valid(nx,ny, maps) and maps[nx][ny] != "X":
                if maps[nx][ny] == "L":
                    bfs(nx,ny, 1, count, visited, q)
                else:
                    bfs(nx,ny, l, count, visited, q)
    return -1