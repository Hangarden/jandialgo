import sys
input = sys.stdin.readline

n = int(input())

minutes = [ list(map(int, input().split())) for _ in range(n) ]
minutes.sort(key= lambda x : (x[1], x[0]))
end = 0
count = 0
for minute in minutes:
    if end <= minute[0]:
        end = minute[1]
        # print(minute)
        count += 1

print(count)