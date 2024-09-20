def solution(s):
    answers = []
    if len(s) == 1:
        return 1
    length = len(s)
    for i in range(1, length):
        answer = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, length + i, i):
            if tmp == s[j: i+j]:
                cnt += 1
            else:
                if cnt >= 2:
                    answer += str(cnt) + ''.join(tmp)
                else:
                    answer += ''.join(tmp)
                tmp = s[j: i+j]
                cnt = 1
        answers.append(len(answer))
    answer = min(answers)

    # print(length)
    return answer