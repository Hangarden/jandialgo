import sys
from collections import deque
import copy





input = sys.stdin.readline

    
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    dxs, dys = [1,-1,0,0], [0,0,1,-1]
    
    def valid(x,y):
        return 0<=x<n and 0<= y < m
    
    things = {}
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
               things['S'] = (i,j)
            elif maps[i][j] == 'L':
               things['L'] = (i,j) 
            elif maps[i][j] == 'E':
               things['E'] = (i,j)
    def dfs_lever(S, L, visited):
        lever_x, lever_y = L[0], L[1]
        start_x, start_y = S[0], S[1]

        visited[start_x][start_y] = 0

        q = deque()
        q.append((start_x,start_y))

        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dxs[i]
                ny = y + dys[i]

                if valid(nx, ny) and maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny)) 


        return visited[lever_x][lever_y]

    # print(things)
    visited_lever = [[-1] * m for _ in range(n)]
    find_lever = dfs_lever(things['S'], things['L'], visited_lever)

    if find_lever == -1:
        answer = -1
        return answer
    else:
        visited_exit = [[-1] * m for _ in range(n)]
        find_exit = dfs_lever(things['L'], things['E'], visited_exit)
        if find_exit == -1:
            answer = -1
            return answer 
        else:
            answer = find_lever + find_exit
    return answer