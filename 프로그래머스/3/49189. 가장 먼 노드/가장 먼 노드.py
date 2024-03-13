from collections import *

def bfs(node, visited,graph):
    visited[node] += 1
    q = deque()
    q.append(node)
    
    while q:
        x = q.popleft()
        
        for a in graph[x]:
            if visited[a] == 0:
                visited[a] = visited[x] + 1
                # print(a, visited[a])
                q.append(a)
                
    return visited
    

def solution(n, edge):
    answer = 0
    visited = [0] * (n+1)
    # visited[0] = True
    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    
    if len(graph[1]) == 0:
        return 0
    else:
        bfs(1,visited,graph)
    # print(visited)
        
    max_val = max(visited)
    
    answer = visited.count(max_val)
    return answer