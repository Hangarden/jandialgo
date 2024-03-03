import sys

sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = [[]]
    
    # 1. 인덱스를 포함한 리스트로 만든다.
    nodeinfo = [(x,y, idx) for idx, (x,y) in enumerate(nodeinfo, 1)]
    # print(nodeinfo)
    nodeinfo.sort(key = lambda x : x[1], reverse = True)
    # print(nodeinfo[0][0])
    # 2. 전위순회, 후위순회를 고려한다. 
    # 3. 전위순회
    def pre(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = nodes[0]
        res = [pivot[2]]
        res += pre([node for node in nodes if node[0] < pivot[0]])
        res += pre([node for node in nodes if node[0] > pivot[0]])
        
        return res
    
    def post(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = nodes[0]
        res = []
        res += post([node for node in nodes if node[0] < pivot[0]])
        res += post([node for node in nodes if node[0] > pivot[0]])
        res.append(pivot[2])
        return res


    # 3-1. 루트 -> 왼 -> 오
    # 왼쪽 노드들의 특징은 root보다 작은 값들의 집합
    # 오른쪽 노드들의 특징은 root보다 큰 값들의 집합
    return pre(nodeinfo), post(nodeinfo)