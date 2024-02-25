def solution(s):
    answer = True
    s = list(s)
    # print(s)
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                answer = False
                return answer
            stack.pop()
            
    if stack:
        answer = False
        return answer
                
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer