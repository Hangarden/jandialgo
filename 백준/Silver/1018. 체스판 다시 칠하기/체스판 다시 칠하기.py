def chess(x,y): # 1, 15
    # print("counting")
    count1 = 0
    count2 = 0


    color1 = "W"
    color2 = "B"
    for i in range(x, x+8): # 1, 9
        for j in range(y, y+8): # 15 23

            if j == y:
                if color1 == maps[i][j]:
                    continue
                else:
                    if maps[i][j] == "B":
                        color1 = "W"
                    else:
                        color1 = "B"
                    count1 += 1
            else:
                if color1 != maps[i][j]:
                    color1 = maps[i][j]
                else:
                    if maps[i][j] == "B":
                        color1 = "W"
                    else:
                        color1 = "B"
                    count1 += 1

    for i in range(x, x + 8):  # 1, 9
        for j in range(y, y + 8):  # 15 23

            if j == y:
                if color2 == maps[i][j]:
                    continue
                else:
                    if maps[i][j] == "B":
                        color2 = "W"
                    else:
                        color2 = "B"
                    count2 += 1
            else:
                if color2 != maps[i][j]:
                    color2 = maps[i][j]
                else:
                    if maps[i][j] == "B":
                        color2 = "W"
                    else:
                        color2 = "B"
                    count2 += 1


    # if x == 0 and y == 5:
    #     print(count1, count2)
    count = min(count1, count2)
    # print(x, y , count)
    return count




a, b = map(int, input().split())

maps = []

for _ in range(a):
    maps.append(list(input()))
min_val = 99999
for i in range(a-7):
    for j in range(b-7): # 13-7 = 6
        min_val = min(min_val, chess(i,j))

print(min_val)

