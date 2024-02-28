n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
a, b,c = 0,0,0

def quad(x, y, n):
    global a, b, c

    color = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                quad(x,y,n//3)
                quad(x,y + n//3 ,n//3)
                quad(x,y + 2*(n//3) ,n//3)
                quad(x+(n//3),y,n//3)
                quad(x+(n//3),y + n//3 ,n//3)
                quad(x+(n//3),y + 2*(n//3) ,n//3)
                quad(x+2 * (n//3),y,n//3)
                quad(x+2 * (n//3),y + n//3 ,n//3)
                quad(x+2 * (n//3),y + 2*(n//3) ,n//3)
                return
    else:
        if color == 1:
            a += 1
        elif color == 0:
            b += 1
        else:
            c += 1
        return

quad(0,0,n)

print(c)
print(b)
print(a)