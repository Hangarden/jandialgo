import sys
from collections import namedtuple
sys.setrecursionlimit(10**5)

Node = namedtuple("Node", ['x','y','id'])

def solution(nodeinfo):
    answer = [[]]
    nodeinfo = [Node(x,y,id) for id, (x,y) in enumerate(nodeinfo, 1)]
    # print(nodeinfo, max(nodeinfo, key = lambda x:x[1]))
    
    def pre(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = max(nodes, key = lambda node:node.y)
        res = [pivot.id]
        res += pre([node for node in nodes if node.x < pivot.x])
        res += pre([node for node in nodes if node.x > pivot.x])
        
        return res
                    
    def post(nodes):
        if len(nodes) < 1:
            return []
        
        pivot = max(nodes, key = lambda node:node.y)
        res = []
        res += post([node for node in nodes if node.x < pivot.x])
        res += post([node for node in nodes if node.x > pivot.x])
        res.append(pivot.id)
        
        return res
    return pre(nodeinfo),post(nodeinfo)