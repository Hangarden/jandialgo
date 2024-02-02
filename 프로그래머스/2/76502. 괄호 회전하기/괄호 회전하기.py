def check(S):
    left = ['{', '(', '[']
    temp = []
    for i in S:
        if i in left:
            temp.append(i)
            # print(temp)
        else:
            if i == ']':
                if temp and temp.pop() == '[':
                    continue
                else:
                    return 0
            elif i == ')':
                if temp and temp.pop() == '(':
                    continue
                else:
                    return 0
            elif i == '}':
                if temp and temp.pop() == '{':
                    continue
                else:
                    return 0
    if temp:
        return 0
    else:
        return 1

def solution(s):
    answer = 0
    s = list(s)
    n = len(s)
    # print(s, n)
    
    for _ in range(n):
        # print(s)
        answer += check(s)
        # print(answer)
        s.append(s.pop(0))
        
    
    return answer