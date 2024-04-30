import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())

# 1인지점을 찾아서 bfs를 실행한다.

# 1인 지점의 좌표를 담아서 모두 bfs한다

array = []

for _ in range(k):
    array.append(list(map(int, input().split())))

tomatos = []
def tomato(array):
    queue = deque()
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 1:
                queue.append([i,j])
    return queue
# print(tomatos)
def checker(array):
    # print(array)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 0:
                return False
    return True
# 퍼질 때 마다 횟수를 +1해서 같이 추가해준다.
def bfs(queue, array):
    dxs = [1,-1,0,0]
    dys = [0,0,1,-1]
    while queue:
        x, y = queue.popleft()
        # print(x,y)
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if 0 <= nx < k and 0 <= ny < n and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append([nx,ny])

def solution(n,k, array):
    answer = 0
    max_val = 0
    queue = tomato(array)
    bfs(queue,array)


    # print(array)
    for i in range(k):
        for j in range(n):
            if array[i][j] ==0:
                print(-1)
                return 
        max_val = max(max_val, max(array[i]))

    if max_val == 1:
        print(0)
        return
    else:
        print(max_val-1)
        return

solution(n,k, array)
