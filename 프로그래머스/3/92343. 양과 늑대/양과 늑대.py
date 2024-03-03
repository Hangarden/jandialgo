answer = []
    
def dfs(node, sheep, wolf, possibles, info, tree):
    # 방문한 곳이 양인지 늑대인지 확인
    global answer
    if info[node] == 0:
        sheep += 1
    else:
        wolf += 1
        
    #양과 늑대 갯수를 확인하고 늑대갯수가 크거나 같다면 전부 잡아먹힘으로 종료
    if sheep > wolf:
        answer.append(sheep)
    else:
        return 
    
    possibles.extend(tree[node])
    for x in possibles:
        dfs(x, sheep, wolf, [i for i in possibles if i != x], info,tree)

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for x,y in edges:
        tree[x].append(y)
    # print(tree)
    dfs(0,0,0,[],info, tree)
    # return 0
    return max(answer)