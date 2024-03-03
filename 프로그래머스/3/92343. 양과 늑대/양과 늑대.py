answer = []
def dfs(node, sheep, wolf, possibles, info, trees):
    global answer
    if info[node] == 0:
        sheep += 1
    else:
        wolf += 1
    
    if sheep > wolf:
        answer.append(sheep)
    else:
        return
        
    possibles.extend(trees[node])
    for i in possibles:
        dfs(i, sheep, wolf, [x for x in possibles if x != i], info,trees)
def solution(info, edges):

    
    trees = [[] for _ in range(len(info))]
    
    for x,y in edges:
        trees[x].append(y)
        
    # print(trees)
    dfs(0,0,0,[], info,trees)
    # print(answer)
    return max(answer)