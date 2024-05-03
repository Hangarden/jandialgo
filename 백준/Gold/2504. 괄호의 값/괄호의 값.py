arr = input()


stack = []
answer = 0
temp = 1
for x in range(len(arr)):
    # print(x, answer, temp, stack)
    if arr[x] == "(":
        temp *= 2
        stack.append(arr[x])
    elif arr[x] == "[":
        temp *= 3
        stack.append(arr[x])
    elif arr[x] == "]":
        if len(stack) == 0 or stack[-1] != "[":
            answer = 0
            break
        if arr[x-1] == "[":
            answer += temp
        temp //= 3
        stack.pop()

    elif arr[x] == ")": # )
        if len(stack) == 0 or stack[-1] != "(":
            answer = 0
            break
        if arr[x-1] == "(":
            answer += temp
        temp //= 2
        stack.pop()
if stack:
    print(0)
else:
    print(answer)


