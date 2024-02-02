n = int(input())

for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    best = [0] * (len(a)-1)
    # print(best)
    count = 1

    while count < len(a):
        if count % 2 == 1:
            best[(count//2)] = a[count]
        else:
            best[-(count//2)] = a[count]
        count += 1
        # print(best)
    max_diff = -1
    for i in range(len(best)):
        max_diff = max(abs(best[i] - best[i-1]), max_diff)

    print(max_diff)