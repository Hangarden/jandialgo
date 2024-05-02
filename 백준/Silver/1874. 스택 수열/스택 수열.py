import sys

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))
# print(nums)
answer = []
def possible(nums):
    global answer
    temp = [0]
    cnt = 1
    for num in nums: # 4
        while temp[-1] < num:
            if cnt > n:
                return "NO"
            answer.append("+")
            temp.append(cnt) # [1,2,3
            cnt += 1
        if temp[-1] == num:
            answer.append("-")
            temp.pop()
        else:
            return "NO"

    return answer

if possible(nums) == "NO":
    print("NO")
else:
    for i in answer:
        print(i)