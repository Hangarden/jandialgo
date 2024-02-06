# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 행렬 만들기


import sys

a, b, c = map(int, sys.stdin.readline().split())


# graph = [[0]*(a+1) for _ in range(a+1)]
# for i in range (b):
#     x,y = map(int,input().split())
#     graph[x][y] = graph[x][y] = 1

graph = [[] for _ in range(a+1)]

for _ in range(b):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()
visited = [False] * (a+1)
visited2 = [False] * (a+1)
def DFS(x): # 1 2 4 3
    visited[x] = True
    print(x, end= " ")
    for i in graph[x]:
        if not visited[i]:
            DFS(i)

from collections import *

def BFS(x):
    queue = deque() # deque 생성
    queue.append(x) # 1추가
    visited2[x] = True

    while queue: # queue에 아무 원소가 존재하지 않을 때 까지
        x = queue.popleft() # 1 빼기 x = 1
        print(x, end= " ") # 1출력 2출력 1
         # 1방문 처리
        for i in graph[x]: # graph[1] = 2,3,4
            if not visited2[i]: # 2
                queue.append(i) # 2,3,4
                visited2[i] = True



DFS(c)
print()
BFS(c)

