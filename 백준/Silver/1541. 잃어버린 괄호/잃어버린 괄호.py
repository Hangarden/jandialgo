x = input()

nums = ""
lst = []
for i in x:
    if i == "+" or i == "-":
        lst.append(nums)
        nums = i
        lst.append(nums)
        nums = ""
    else:
        nums += i

lst.append(nums)
# print(lst)

# 홀수인덱스는 숫자
# 짝수 인덱스는 연산자
temp = 0
answer = 0
stack = []
for i in lst:
    if i == "-":
        answer -= temp
        temp = 0
        stack = ["-"]
    else:
        if len(stack) >= 1 and stack[0] == "-":
            if i != "+":
                temp += int(i)
        else:
            if i != "+":
                answer += int(i)

if len(stack) >= 1 and stack[0] == "-":
    answer -= temp
print(answer)