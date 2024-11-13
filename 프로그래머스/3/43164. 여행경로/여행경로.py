def solution(tickets):
    
    def ticket(start, end, visited, path):
        if visited.count(True) == len(visited):
            answer.append(path) 
            return 
        for idx in range(len(visited)):
            if not visited[idx] and tickets[idx][0] == end:
                visited[idx] = True
                ticket(tickets[idx][0], tickets[idx][1], visited, path + [tickets[idx][1]])
                visited[idx] = False
                
    answer = []
    length = len(tickets)
    start, end = "", ""
    visited = [False for _ in range(length)]
    print(visited)
    for idx in range(length):
        start = tickets[idx][0]
        end = tickets[idx][1]
        if start == "ICN":
            visited[idx] = True
            ticket(start, end, visited, [start, end])
            visited[idx] = False
    
    answer.sort()
        
    return answer[0]