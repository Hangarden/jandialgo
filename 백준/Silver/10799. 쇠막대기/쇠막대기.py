lst = input()

pipe = []

raiser = []

stack = []
answer = 0
for i in range(len(lst)):
    if lst[i] == "(":
        stack.append(lst[i])
    else: # )
        if lst[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
# ( ) ( ( ( ( ) ( ) ) (  (  )   )  (   )   )   ) ( ( ) )
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13  14  15  16  17
print(answer)
# print(pipe)


