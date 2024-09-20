def game(level, diff, times):
    total = 0
    # 원소갯수만큼 순회
    for i in range(len(diff)):
        
        # diff가 level보다 높다면 다시 맞추어야 함
        if diff[i] > level:
            repeat = diff[i] - level
            total += ( (times[i-1] + times[i]) * repeat ) + times[i]
        # 낮다면 넘어감
        else:
            total += times[i]
        # print(level, total)
    return total
# def binary(min_val, max_val, answer):
    
#     while (min_val <= max_val):
#         mid = (min_val + max_val) // 2

#         x = game(mid)

#         if x >= answer:
#             opt_level = min(opt_level, mid)
#             min_val = mid + 1
#         else:
#             max_val = mid -1
            
#     return opt_level
    
def solution(diffs, times, limit):
    min_val = min(diffs)
    max_val = max(diffs)
    opt_level = float('inf')
    while (min_val <= max_val):
        mid = (min_val + max_val) // 2

        x = game(mid, diffs, times)

        # 소요시간이 limit보다 작거나 같다면 값을 줄여본다.
        if x <= limit:
            opt_level = min(opt_level, mid)
            max_val = mid - 1
        # 크다면 값을 늘려야함으로 최댓값을 늘림
        else:
            min_val = mid + 1

    answer = opt_level
    return answer