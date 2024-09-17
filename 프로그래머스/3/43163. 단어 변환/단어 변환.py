from collections import *
def solution(begin, target, words):
    answer = 0
    word_len = len(begin)
    def canChange(word, x):
        diff = 0
        
        for i in range(word_len):
            if word[i] != x[i]:
                diff += 1
        
        if diff == 1:
            return True
        
        else:
            return False
    
    def bfs():
        
        if target not in words:
            return 0
        q = deque()
        
        q.append((begin,0))
        
        while q:
            x,depth = q.popleft()
            
            if x == target:
                return depth
            
            for word in words:
                if canChange(x, word):
                    q.append([word, depth+1])
    answer = bfs()
    return answer