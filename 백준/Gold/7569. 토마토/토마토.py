import sys
from collections import deque
input = sys.stdin.readline
def tomato():
    N, M, H = map(int, input().split())

    boxes = [[] for _ in range(H)]
    for i in range(H):
        for _ in range(M):
            boxes[i].append(list(map(int,input().split())))

    # print(boxes)

    tomatos = deque()

    for x in range(H):
        for y in range(M):
            for z in range(N):
                if boxes[x][y][z] == 1:
                    tomatos.append((x,y,z))

    if len(tomatos) == (N*M*H):
        return 0
    def valid(x):
        a = False
        if 0<= x[0] < H and 0 <= x[1] < M and 0 <= x[2] < N and boxes[x[0]][x[1]][x[2]] == 0:
            a = True
        return a

    while tomatos:

        box, x, y = tomatos.popleft()


        up = (box,x-1,y)
        down = (box,x+1,y)
        left = (box,x,y-1)
        right = (box,x,y+1)
        above = (box-1,x,y)
        below = (box+1,x,y)

        if valid(up):
            boxes[up[0]][up[1]][up[2]] = boxes[box][x][y] + 1
            tomatos.append(up)

        if valid(down):
            boxes[down[0]][down[1]][down[2]] = boxes[box][x][y] + 1
            tomatos.append(down)

        if valid(left):
            boxes[left[0]][left[1]][left[2]] = boxes[box][x][y] + 1
            tomatos.append(left)

        if valid(right):
            boxes[right[0]][right[1]][right[2]] = boxes[box][x][y] + 1
            tomatos.append(right)

        if valid(above):
            boxes[above[0]][above[1]][above[2]] = boxes[box][x][y] + 1
            tomatos.append(above)

        if valid(below):
            boxes[below[0]][below[1]][below[2]] = boxes[box][x][y] + 1
            tomatos.append(below)

    # print(boxes)

    max_days = 0
    for layer in boxes:
        for row in layer:
            for tomato in row:
                if tomato == 0:  # 익지 않은 토마토가 있는 경우
                    return -1
                max_days = max(max_days, tomato)

    return max_days - 1

print(tomato())