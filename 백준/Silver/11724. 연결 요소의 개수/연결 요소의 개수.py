from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)
visited = [0] * (n+1)
# print(visited)
count = 0

def bfs(now):
    visited[now] = 1

    q = deque()
    q.append(now)
    while q:
        x = q.popleft()
        # visited[x] = True

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

for i in range(1, n+1):
    if visited[i] == 0:
        count += 1
        bfs(i)

print(count)

