from collections import deque
import copy


def find_lever(count_maps, S, visited, origin_maps):
    global answer
    q = deque()
    q.append(S)
    visited[S[0]][S[1]] = True

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if 0 <= nx < len(count_maps) and 0 <= ny < len(count_maps) and not visited[nx][ny] and origin_maps[nx][
                ny] != "X":
                q.append((nx, ny))
                visited[nx][ny] = True
                count_maps[nx][ny] = count_maps[x][y] + 1
    return count_maps


def find_exit(count_maps, L, visited, origin_maps):
    global answer
    q = deque()
    q.append(L)
    visited[L[0]][L[1]] = True

    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if 0 <= nx < len(count_maps) and 0 <= ny < len(count_maps) and not visited[nx][ny] and origin_maps[nx][
                ny] != "X":
                q.append((nx, ny))
                visited[nx][ny] = True
                count_maps[nx][ny] = count_maps[x][y] + 1


def solution(maps):
    answer = 0
    print(maps)
    maps_size = len(maps)
    visited = [[False] * maps_size for _ in range(maps_size)]
    lever_map = [[0] * maps_size for _ in range(maps_size)]

    # print(visited)
    for i in range(maps_size):
        for j in range(maps_size):
            if maps[i][j] == "L":
                L = [i, j]
            elif maps[i][j] == "S":
                S = [i, j]
            elif maps[i][j] == "E":
                E = [i, j]

    # print(L, S, E)
    visited2 = copy.deepcopy(visited)
    visited3 = copy.deepcopy(visited)
    test_map = copy.deepcopy(lever_map)
    after_lever = find_lever(test_map, S, visited2, maps)

    if after_lever == lever_map:
        answer = -1
        return answer

    find_exit(after_lever, L, visited3, maps)

    answer = after_lever[E[0]][E[1]]
    return answer