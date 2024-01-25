def solution(n,a,b):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while a != b:
        
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    return answer