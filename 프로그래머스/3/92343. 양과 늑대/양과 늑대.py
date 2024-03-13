answer = 0
def solution(info, edges):

    
    n = len(info)
    
#     tree = [[] for _ in range(n)]
    
#     for a, b in edges:
#         tree[a].append(b)
        
    visited = [False] * n
    visited[0] = True
    # print(visited)
    
    def dfs(sheep, wolf):
        global answer
        if sheep <= wolf:
            return
        else:
            answer = max(answer, sheep)
            
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 1:
                    dfs(sheep, wolf + 1)
                else:
                    dfs(sheep + 1, wolf)
                visited[c] = 0
                
    dfs(1,0)
                
    return answer