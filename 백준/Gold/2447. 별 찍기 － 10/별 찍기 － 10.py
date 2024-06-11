def draw_star(n):
    if n == 1:
        return ['*']

    stars = draw_star(n // 3)  # n//3 크기의 이전 패턴을 만듦
    result = []

    for i in range(3):
        for s in stars:
            if i == 1:  # 가운데 부분일 때
                result.append(s + ' ' * (n // 3) + s)
            else:
                result.append(s * 3)

    return result

n = int(input())
ans = draw_star(n)
for a in ans:
    print(a)
