import sys

input = sys.stdin.readline

n = int(input())

def find(name):
    if parent[name] == name:
        return name
    else:
        p = find(parent[name])
        parent[name] = p
        return p

def union(name1, name2):
    name1, name2 = find(name1), find(name2)

    if name1 != name2:
        parent[name2] = name1
        number[name1] += number[name2]

    return print(number[name1])

for _ in range(n):
    parent, number = {}, {}
    networks = int(input())
    for _ in range(networks):
        name1, name2 = input().split()
        if name1 not in parent.keys():
            parent[name1] = name1
            number[name1] = 1

        if name2 not in parent.keys():
            parent[name2] = name2
            number[name2] = 1

        union(name1, name2)
        # print(number[name1])