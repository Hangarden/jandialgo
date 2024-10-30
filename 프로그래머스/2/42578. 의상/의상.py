def solution(clothes):
    answer = 0
    

    kinds = {}
    
    for clothes, kind in clothes:
        if kind not in kinds:
            kinds[kind] = 1
        else:
            kinds[kind] += 1
    print(kinds)
    sum = 1
    for x in kinds.values():
        sum *= (x+1)
        
    answer = sum -1 
    
    # for x in kinds:
    #     print(x)
    
    return answer