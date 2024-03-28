import itertools

def solution(clothes):
    answer = 1
    dict = {}
    for name, kind in clothes:
        
        if kind not in dict.keys():
            dict[kind] = [name]
        
        else:
            dict[kind].append(name) 
        
    print(dict)
    
    for x in dict.keys():
        answer *= (len(dict[x]) + 1)
        # print(x, len(dict[x]))
    
    return answer -1