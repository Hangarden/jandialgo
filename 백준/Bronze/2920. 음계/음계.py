
lst = list(map(int, input().split()))

# print(lst)

if lst == sorted(lst):
    print("ascending")
elif lst == sorted(lst, reverse= True):
    print("descending")
else:
    print("mixed")