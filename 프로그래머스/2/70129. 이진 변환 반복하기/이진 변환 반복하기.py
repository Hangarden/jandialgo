def solution(s):
    answer = []
    count = 0
    cycle = 0
    # 사이클
    print(s)
    # 0의 갯수를 셈
    
    while (s != '1'):
        
        x = s.count('0')
        # print(x)
        count += x
        # s에 있는 0 모두 제거
        s = s.replace('0', '')
        print(s)
        # 0을 제거한 뒤 길이 계산 
        x = len(s)
        # 해당길이를 이진수로
        s = bin(x)[2:]
        print(s)
        cycle += 1
    answer = [cycle, count]
    return answer