a,b = 0,0
def quad_tree(x, y, n, arr):
    global a
    global b
    color = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != arr[i][j]:  # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
                # result.append("(") # 4분면으로 나눌때 괄호를 친다.
                quad_tree(x, y, n // 2, arr)
                quad_tree(x, y + n // 2, n // 2, arr)
                quad_tree(x + n // 2, y, n // 2, arr)
                quad_tree(x + n // 2, y + n // 2, n // 2, arr)
                return

    else:
        if color == 1:
            a += 1
        else:
            b += 1

    return
            
    

def solution(arr):
    answer = []
    # print(arr)
    global a,b
    quad_tree(0, 0, len(arr), arr)
    answer.append(b)
    answer.append(a)
    return answer



        