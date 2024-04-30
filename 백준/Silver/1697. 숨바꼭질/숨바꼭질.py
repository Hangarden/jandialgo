from collections import deque
N, K = map(int, input().split())

def bfs(n):
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == K:
            return visited[v]
        for i in (v - 1, v+ 1, 2 * v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)



visited = [0 for _ in range(100001)]
# print(visited)
print(bfs(N))
