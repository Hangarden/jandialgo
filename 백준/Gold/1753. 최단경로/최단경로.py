import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V+1)]

# 그래프 생성
for _ in range(E):
    start ,arrive, distance = map(int, input().split())
    graph[start].append((arrive, distance))

# print(graph)

visited = [False] * (V+1)
distance = [9999999999999] * (V+1)
# print(visited)
# print(distance)

# def get_minimumdis():
#     min_val = 9999999999999
#     index = 0
#     for i in range(1, V+1):
#         if distance[i] < min_val and not visited[i]:
#             min_val = distance[i]
#             index = i
#
#     return index

def dajikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 시작점 방문 처리
    # visited[start] = True
    while q:
    # 시작점에서 갈 수 있는 노드들의 최단 거리 갱신
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

        # for x in graph[start]:
        #     distance[x[0]] = x[1]
        #
        # for _ in range(V-1):
        #     # 시작점에서 가장 짦은 노드가 나올 것임
        #     node = get_minimumdis()
        #     visited[node] = True
        #     # 노드에서 갈 수 있는 최단 거리를 갱신해야 한다
        #     for i in graph[node]:
        #         # 기존 거리보다 최단 노드에서 간 거리를 더한 것이 짦다면 갱신
        #         if distance[i[0]] > distance[node] + i[1]:
        #             distance[i[0]] = distance[node] + i[1]

dajikstra(K)
distance = distance[1:]
# print(distance)
for i in distance:
    if i == 9999999999999:
        print('INF')
    else:
        print(i)
# print(visited)
# print(distance)
