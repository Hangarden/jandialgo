min_val = 999999
def solution(begin, target, words):
    
    def possible(cur, word):
        count = 0
        for idx in range(len(word)):
            if word[idx] != cur[idx]:
                count += 1

        if count == 1:
            return True
        else:
            return False
    def back(visited, cur, n):
        global min_val
        if cur == target:
            min_val = min(min_val, n)
            return
        if len(visited) == len(words):
            return 

        for word in words:
            if possible(cur, word):
                if word not in visited:
                    visited.append(word)
                    back(visited, word, n+1)
                    visited.pop()
    answer = 0
    
    back([], begin, 0)
    
    if min_val == 999999:
        answer = 0
    else:
        answer = min_val
        
    return answer