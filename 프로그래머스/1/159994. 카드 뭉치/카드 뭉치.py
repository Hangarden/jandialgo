from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1.popleft()
            continue
        elif cards2 and cards2[0] == word:
            cards2.popleft()
            continue
        else:
            answer = 'No'
            break
    else:
        answer = 'Yes'
    return answer