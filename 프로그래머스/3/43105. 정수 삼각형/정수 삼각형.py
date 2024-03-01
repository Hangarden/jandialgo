# def ddp(triangle):
    
#     for i in range(len(trianlge)):

def solution(triangle):
    answer = 0
    # triangle = [[id,x] for id, x in enumerate(triangle)]
    # print(len(triangle[-1]))
    
    for j in range(1, len(triangle)): 
        for i in range(len(triangle[j])):
            if i == 0:
                triangle[j][i] = triangle[j-1][i] + triangle[j][i]
            elif i == len(triangle[j]) - 1:
                triangle[j][-1] = triangle[j-1][-1] + triangle[j][-1]
            else:
                triangle[j][i] = triangle[j][i] + max(triangle[j-1][i-1], triangle[j-1][i])
    # for i in range(len(triangle)):
        
    # dp = [] for _ in range(i) for i
    # dp = [[] for _ in range(i) for i in range(len(triangle))]
    # print(dp)
    return max(triangle[-1])
    # return max(lst[-1])