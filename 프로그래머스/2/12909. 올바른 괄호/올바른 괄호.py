def solution(s):
    answer = True
    stack = []
    # print(s)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) >= 1:
        return False

    return answer