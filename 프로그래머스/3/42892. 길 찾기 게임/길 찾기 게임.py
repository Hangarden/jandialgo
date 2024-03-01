import sys

sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    answer = [[]]
    
    nodeinfo = [[x,y,id] for id, (x,y) in enumerate(nodeinfo, 1)]
    # print(nodeinfo)
    
    def pre(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = max(nodes, key = lambda x:x[1])
        res = [pivot[2]]
        res += pre([node for node in nodes if node[0] < pivot[0]])
        res += pre([node for node in nodes if node[0] > pivot[0]])
        return res
    
    def post(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = max(nodes, key = lambda x:x[1])
        res = []
        res += post([node for node in nodes if node[0] < pivot[0]])
        res += post([node for node in nodes if node[0] > pivot[0]])
        res.append(pivot[2])
        return res
    return pre(nodeinfo), post(nodeinfo)
    # test_left = [node for node in nodeinfo if node[0] < pivot[0]]
    # test_right = [node for node in nodeinfo if node[0] > pivot[0]]
    # print(test_left)
    # print(pivot)
    # print(test_right)
    
    # def 
    