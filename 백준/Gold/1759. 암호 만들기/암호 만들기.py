import sys
from itertools import *
input = sys.stdin.readline

l, c = map(int, input().split())

lst = list(input().split())
lst.sort()

# print(lst)

a = list(combinations(lst, l))
# print(len(a))
moeum = ['a', 'e', 'i', 'o', 'u']

for x in a: # a c i s
    M, J = 0,0
    for y in x:
        # print(y)
        if y in moeum:
            M +=1
        else:
            J +=1
    if M >= 1 and J >= 2:
        print(''.join(x))