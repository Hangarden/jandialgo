import heapq

# def dajikstra(start):
#     q = [] 
#     heapq.heappush(q, (0,start))
#     distance[start] = 0
    
#     while q:
#         dist, now = heapq.heappop(q)
        
#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + i[1]
#             if distance[i[0]] > cost:
#                 distance[i[0]] = cost
#                 road[i[0]].append(i[0])
#                 heapq.heappush(q, (cost, i[0]))

def solution(n, s, a, b, fares):
    road = [[] for _ in range(n+1)]
    answer = 0
    
    
    # 양방향 그래프 구현
    graph = [[] for _ in range(n+1)]
    
    for x in fares:
        graph[x[0]].append((x[1],x[2]))
        graph[x[1]].append((x[0],x[2]))
    # print(graph)
    
    # 최단거리 
    def dajikstra(s):
        distance = [float('inf') for _ in range(n+1)]
        q = [] 
        heapq.heappush(q, (0,s))
        distance[s] = 0

        while q:
            
            dist, now = heapq.heappop(q)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    road[i[0]].append(i[0])
                    heapq.heappush(q, (cost, i[0]))
                    
        return distance
    D = [0] + [ dajikstra(i) for i in range(1,n+1) ]
    # print(D)
    path = float('inf')
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
    
    return path