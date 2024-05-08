n, m = map(int, input().split())

lst = list(map(int, input().split()))
answer = 0
if m == 1:
    answer += n
    for i in range(n):
        
        if i <= n-4 and lst[i] == lst[i+1] == lst[i+2] == lst[i+3]:
            answer += 1

elif m == 2:
    for i in range(n):
        # 11
        if i <= n -2 and lst[i] == lst[i+1]:
            answer += 1

elif m == 3:
    for i in range(n):
        # 110

        if i <= n - 3 and lst[i] + 1 == lst[i + 1] + 1 == lst[i + 2]:
            answer += 1
        # 01
        if i <= n - 2 and lst[i] == lst[i + 1] + 1:
            answer += 1

elif m == 4:
    for i in range(n):
        # 011

        if i <= n - 3 and lst[i] == lst[i + 1] + 1 == lst[i + 2] + 1:
            answer += 1
        # 10
        if i <= n - 2 and lst[i] + 1  == lst[i + 1]:
            answer += 1

elif m == 5:
    for i in range(n):
        # 111

        if i <= n - 3 and lst[i] == lst[i + 1] == lst[i + 2] :
            answer += 1
        #010
        if i <= n - 3 and lst[i] == lst[i + 1] + 1 == lst[i + 2]:
            answer += 1
        # 10
        if i <= n - 2 and lst[i] + 1  == lst[i + 1]:
            answer += 1
        # 01
        if i <= n - 2 and lst[i] == lst[i + 1] + 1:
            answer += 1

elif m == 6:
    for i in range(n):
        # 111

        if i <= n - 3 and lst[i] == lst[i + 1] == lst[i + 2]:
            answer += 1
        # 01
        if i <= n - 2 and lst[i] == lst[i + 1] + 2:
            answer += 1
        # 100 180도
        if i <= n - 3 and lst[i] + 1 == lst[i + 1] == lst[i + 2]:
            answer += 1

        #11
        if i <= n -2 and lst[i] == lst[i+1]:
            answer += 1

else:
    for i in range(n):
        # 111

        if i <= n - 3 and lst[i] == lst[i + 1] == lst[i + 2]:
            answer += 1
        # 10
        if i <= n - 2 and lst[i] + 2== lst[i + 1]:
            answer += 1
        # 001
        if i <= n - 3 and lst[i] == lst[i + 1] == lst[i + 2] + 1:
            answer += 1

        # 11
        if i <= n - 2 and lst[i] == lst[i + 1]:
            answer += 1

# elif m == 4:
#
#     for i in range(n):
#         # 011
#
        # if i <= n - 3 and lst[i] + 1 == lst[i + 1] == lst[i + 2]:
        #     answer += 1
#         # 10
#         if i <= n - 2 and lst[i] == lst[i + 1] + 1:
#             answer += 1

# elif m == 5:
#     for i in range(n):
#
# elif m == 6:
#     for i in range(n):
#
# else:

print(answer)


