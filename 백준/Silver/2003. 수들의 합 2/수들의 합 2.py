n, m = map(int, input().split())

data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0
# 0 -> interval_sum -= data[0] = 5
# 1 -> interval_sum = 5 -> count +=1 -> interval_sum - data[1] = 3
# 2 -> end = 4 -> interval_sum = 5 -> count += 1  -> interval_sum - data[2] -> 2
# 3 ->
# start를 차례대로 증가시키며 반복
for start in range(n): # 0 1 2 3 4
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n: #  0 < m 0 <
        interval_sum += data[end] #3
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start] # 3

print(count)