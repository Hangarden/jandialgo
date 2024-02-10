N = int(input())

array = [1] * (N+1)


for i in range(2,N+1):
    array[i] = array[i-1] * 2 + 1


count = 0
def hanoi(n, start, target, assist):
    if n == 1:
        print(start, target)
        return
    hanoi(n-1, start, assist, target)
    print(start, target)
    hanoi(n-1, assist, target, start)
print(array[N])
hanoi(N, 1,3,2)