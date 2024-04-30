def solution(numbers, target):
    answer = 0
    print(len(numbers))
    def back(n, sums):
        nonlocal answer
        if n == len(numbers):
            if sums == target:
                answer += 1
            return
        
        sums += numbers[n]
        back(n+1, sums)
        sums -= (2 * numbers[n])
        back(n+1, sums)
        
    back(0,0)
    
    return answer