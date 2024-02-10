n = int(input())
array = list(map(int, input().split()))

array.sort()
# print(array)


def weight(array):
    max = 0
    for i in array:
        if max + 1 < i:
            return (max+1)
            # break
        else:
            max += i
            # print(max+1)
            # print(max)
    return (max+1)
print(weight(array))