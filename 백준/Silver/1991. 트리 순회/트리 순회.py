
import sys
input = sys.stdin.readline
#
tree = {}
n = int(input())
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

# print(tree)


def preorder(nodes, start):

    if start != '.':
        print(start, end = "")
        preorder(nodes, nodes[start][0])
        preorder(nodes, nodes[start][1])
    else:
        return

def midorder(nodes, start):

    if start != '.':
        midorder(nodes, nodes[start][0])
        print(start, end="")
        midorder(nodes, nodes[start][1])
    else:
        return
def lastorder(nodes, start):

    if start != '.':
        lastorder(nodes, nodes[start][0])
        lastorder(nodes, nodes[start][1])
        print(start, end="")
    else:
        return


def setorder(nodes, start):
    
    preorder(tree, 'A')
    print()
    midorder(tree, 'A')
    print()
    lastorder(tree, 'A')
    
setorder(tree, 'A')