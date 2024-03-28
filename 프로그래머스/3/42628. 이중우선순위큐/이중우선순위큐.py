from heapq import heappop, heappush
def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    for operation in operations:
        x, y  = operation.split(" ")
        y = int(y)
        if x == "I":
            heappush(max_heap, -y)
            heappush(min_heap, y)
        elif x == "D":
            if y == -1 and min_heap: 
                min_val = heappop(min_heap)
                max_heap.remove(-min_val)
                
            elif y == 1 and max_heap:
                max_val = heappop(max_heap)
                min_heap.remove(-max_val)
    if len(min_heap) <= 0:
        return [0,0]
    else:
        return[max(min_heap), min(min_heap)]