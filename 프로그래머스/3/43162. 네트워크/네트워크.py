def dfs(idx):
    visited[idx] = True
    
    for z, x in enumerate(computers[idx]):
        if not visited[z] and x==1:
            dfs(z)
        

def solution(n, computers):
    answer = 0
    def dfs(idx):
        visited[idx] = True
    
        for z, x in enumerate(computers[idx]):
            if not visited[z] and x==1:
                dfs(z)
    visited = [False] * (n)
    
    for idx, computer in enumerate(computers):
        # visited[idx] = True
        for idx, x in enumerate(computer):
            if not visited[idx] and x == 1:
                dfs(idx)
                answer += 1
    return answer









# def dfs(x,n,visited, computers):
#     visited[x] = True
    
#     for i in range(n):
#         if visited[i] == False and computers[x][i] == 1:
#             dfs(i, n,visited,computers)

# def solution(n, computers):
    
#     answer = 0
#     visited = [False] *n
#     # print(visited)
#     for i in range(n):
#         for j in range(n):
#             if not visited[i]:
#                 dfs(i,n,visited,computers)
#                 answer += 1
#     return answer