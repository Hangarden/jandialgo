def solution(triangle):
    answer = 0
    
    for j in range(1, len(triangle)): 
        for i in range(len(triangle[j])):
            if i == 0:
                triangle[j][i] = triangle[j-1][i] + triangle[j][i]
            elif i == len(triangle[j]) - 1:
                triangle[j][-1] = triangle[j-1][-1] + triangle[j][-1]
            else:
                triangle[j][i] = triangle[j][i] + max(triangle[j-1][i-1], triangle[j-1][i])

    return max(triangle[-1])
