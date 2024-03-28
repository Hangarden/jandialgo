import heapq

def solution(operations):
    lst1 = []  # 최소 힙
    lst2 = []  # 최대 힙 (값을 음수로 변환하여 저장)
    
    for operation in operations:
        op, value = operation.split()
        value = int(value)
        
        if op == "I":
            heapq.heappush(lst1, value)
            heapq.heappush(lst2, -value)
        elif op == "D":
            if value == 1 and lst2:  # 최댓값 제거
                max_val = -heapq.heappop(lst2)
                lst1.remove(max_val)
            elif value == -1 and lst1:  # 최솟값 제거
                min_val = heapq.heappop(lst1)
                lst2.remove(-min_val)
    
    # 교집합을 구하기 위해 lst1과 lst2를 집합으로 변환
    set1 = set(lst1)
    set2 = {-x for x in lst2}  # lst2의 원소를 원래 값으로 변환하여 집합 생성
    common_elements = set1 & set2  # 교집합

    if common_elements:
        return [max(common_elements), min(common_elements)]
    else:
        return [0, 0]

# import heapq

# def solution(operations):
#     answer = []
#     lst1 = []
#     lst2 = []
    
#     for operation in operations:
#         x, y = operation.split(" ")
#         y = int(y)
#         if x == "I":
#             heapq.heappush(lst1, y) # 최소 힙
#             heapq.heappush(lst2, -y) # 최대 힙
#         elif x == "D":
#             if y == 1 and lst2: # 최댓값제거
#                 heapq.heappop(lst2) # 최대 힙
#             if y == -1 and lst1: # 최솟값 제거
#                 heapq.heappop(lst1) # 최소 힙
                
    
#     print(lst1, lst2)
#     return answer

# import heapq

# def solution(operations):
#     min_heap = []
#     max_heap = []
    
#     for operation in operations:
#         op, num = operation.split()
#         num = int(num)
        
#         if op == "I":
#             heapq.heappush(min_heap, num)
#             heapq.heappush(max_heap, -num)
#         elif op == "D":
#             if num == 1 and max_heap:  # 최댓값 삭제
#                 max_val = -heapq.heappop(max_heap)
#                 min_heap.remove(max_val)
#             elif num == -1 and min_heap:  # 최솟값 삭제
#                 min_val = heapq.heappop(min_heap)
#                 max_heap.remove(-min_val)
    
#     if min_heap and max_heap:
#         return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
#     else:
#         return [0, 0]