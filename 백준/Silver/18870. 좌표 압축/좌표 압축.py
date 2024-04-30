N = int(input())

x = list(map(int, input().split()))
a = sorted(x)
# print(x)
# print(a)
# x = sorted(set(x), reverse= True)

dict = {}
idx = 0
for value in a:
    if value not in dict.keys():
        dict[value] = idx
        idx += 1
    else:
        continue

for i in x:
    print(dict[i], end=" ")