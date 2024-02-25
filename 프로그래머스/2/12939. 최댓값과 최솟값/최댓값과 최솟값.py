def solution(s):
    answer = ''
    a = list(map(int, s.split(" ")))
    print(a)
    x = min(a)
    y = max(a)
    answer = str(x) + " " + str(y)
    # answer = x + " " + y
    return answer