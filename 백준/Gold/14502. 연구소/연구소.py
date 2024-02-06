import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
def make_wall(count):
    # print(count)
    global max_val
    if count == 3:
        # 정상적으로 벽을 세우는 지 확인 -> 확인 완료
        # print(array)
        test_map = copy.deepcopy(array)
        x = bfs(test_map)

        max_val = max(max_val, x)
        return

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                make_wall(count + 1)
                # make_wall(array, count + 1)
                array[i][j] = 0
def valid(x, y):

    return 0<= x < n and 0 <= y < m
def bfs(array):

    # 바이러스를 담을 큐
    q = deque()

    # 바이러스가 있는 좌표를 q에 담는다
    for i in range(n):
        for j in range(m):
            if array[i][j] == 2:
                q.append((i,j))

    # bfs를 이용한 완전탐색 전파
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if valid(nx,ny) and array[nx][ny] == 0:
                array[nx][ny] = 2 # 전파
                q.append((nx,ny))

    # 전파 완료 후 안전영역 갯수 탐색 안전영역은 숫자 0인 칸의 수를 세면 된다.

    count =0

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count += 1

    return count



max_val = 0



array = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [-1,1,0,0],[0,0,-1,1]
make_wall(0)
print(max_val)