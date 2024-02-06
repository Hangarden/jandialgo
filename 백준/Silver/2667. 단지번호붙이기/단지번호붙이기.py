# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3
# 7
# 8
# 9

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input())))
visits = [[False] * n for _ in range(n)]
# 25 * 25 * 5
counts = 0
def DFS(x,y):
    dxs, dys = [-1,1,0,0], [0,0,-1,1]
    visits[x][y] = True
    global counts
    counts += 1
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]

        if 0<= nx < n and 0<= ny < n and not visits[nx][ny] and array[nx][ny] ==1:
            DFS(nx,ny)
        else:
            continue

    return counts

count = 0
array2 = []
for x in range(n):
    for y in range(n):
        if array[x][y] == 1 and not visits[x][y]:
            num = DFS(x,y)
            array2.append(num)
            count += 1
            counts = 0

print(count)

array2.sort()

for i in array2:
    print(i)