min_val = float('inf')
def solution(n, wires):
    global min_val
    answer = -1
    # print(n, wires)
    # print(wires)
    for i in range(n-1):
        x,y = wires.pop(0)
        # print(wires)
        min_val = min(min_val, make(n, wires, x, y))
        # print(min_val)
        wires.append([x,y])
        # print(wires)
    answer = min_val
    return answer

def make(n, wires, x,y):
    tree = [[] for _ in range(n+1)]
    for i in wires:
        tree[i[0]].append(i[1])
        tree[i[1]].append(i[0])
    # print(tree, x, y)
    a = dfs(x, [False] * (n+1), tree)
    # print("a ", visited)
    # print(dfs(x-1, visited, 1,tree))
    b = dfs(y, [False] * (n+1), tree)
    # print("b ", visited)
    # print(dfs(y-1, visited, 1,tree))
    # return
    # print(a, b, abs(a-b))
    return abs(a - b)

def dfs(first, visited, tree):
    
    visited[first] = True
    for i in tree[first]:
        if not visited[i]:
            dfs(i, visited, tree)
    # print(visited)
    return sum(visited)
            