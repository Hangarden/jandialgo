n, m = map(int, input().split())

trees = list(map(int, input().split()))

end = max(trees)

start = 1

x = []
while start <= end:
    mid = (start + end) // 2
    answer = 0
    for tree in trees:
        if tree >=  mid:
            answer += tree - mid

    if answer >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# print(max(x))

