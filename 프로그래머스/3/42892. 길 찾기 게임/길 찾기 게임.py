import sys; sys.setrecursionlimit(10001)
from collections import namedtuple
# class Node(object):
#     def __init__(self, info):
#         self.num = info[2]
#         self.pos = info[:2]
#         self.left = None
#         self.right = None
        
# class Node(object):
#     def __init__(self, info):
#         self.num = info[2]
#         self.pos = info[:2]
#         self.left = None
#         self.right = None
        
# Node = namedtuple('Node', ['x', 'y', 'id'])
Node = namedtuple('Node', ['x','y','id'])
def solution(nodeinfo):
    answer = [[]]
    nodes = [Node(x,y,idx)for idx,(x,y) in enumerate(nodeinfo, 1)]
    # print(nodes)
    
    def pre(nodes):
        if len(nodes) < 1:
            return [node.id for node in nodes]
        
        pivot = max(nodes, key = lambda nodes :nodes.y)
        res = [pivot.id]
        res += pre([node for node in nodes if node.x < pivot.x])
        res += pre([node for node in nodes if node.x > pivot.x])
        
        return res
    
    def post(nodes):
        if len(nodes) < 1:
            return [node.id for node in nodes]
        
        pivot = max(nodes, key = lambda nodes :nodes.y)
        res = []
        res += post([node for node in nodes if node.x < pivot.x])
        res += post([node for node in nodes if node.x > pivot.x])
        res.append(pivot.id)
        return res
    
    return pre(nodes), post(nodes)