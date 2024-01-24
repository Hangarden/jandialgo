# N <= 20임으로 스타트팀이냐 링크팀이느냐로 나누었을 때 경우가 있다 따라서 2가지 경우의 수가 있고ㅗ N = 20이니
# 총 경우의 수는 2의 20제곱이라고 볼 수 있다. 2의 20제곱은 10의 6제곱으로 1억 미만임으로 백투레킹으로 접근할 수 있다

# 트리구조로 살펴보면 1번 선수가 스타트팀일 때 링크 팀일 떄 나 뉘고 2번 선수가 스타트팀일 때 링크 팀일 때로 나뉜다
# 두 팀의 인원수가 같다는 조건은 M/2명으로 이루어졌다 하니 두 팀의 인원이 같을 때 경기가 시작된다.

# 백트레킹을 사용하여 1번선수가 스타트 팀일 때 링크팀일때인 경우를 모두 가정하고 이후 2번선수가 스타트팀일 때 링크 팀일때 모두 고려한다
# 나눈 경우중 선수번호가 N보다 커졌을 때   a팀과 b팀의 길이가 같은 경우 두 팀의 능력치를 구하고 두 팀의 능력치 차이의 절댓값을 구한뒤 계속 최솟값을
# 갱신한다

N = int(input())
# 능력치 map 입력
ability_map = [list(map(int, input().split())) for _ in range(N)]
M = N//2
answer = 10e11
# 팀 나누기


def dfs(x, alst,blst):
    # print("alst : ", alst)
    # print("blst : ", blst)

    # 함수에서 answer 변수를 사용함으로
    global answer
    # N번 선수까지 팀 배정을 마친 경우에는 더이상 배정할 수 없음으로 팀인원수가 같은지 체크하고 같지 않다면 종료
    if x >= N:
        # a팀과 b팀의 인원수가 같은 경우 능력치 차이를 구해야한다.
        if len(alst) == len(blst):
            answer = min(answer, cal(alst, blst))
        return  # 같지 않더라도 종료시켜야 하기 때문에
    dfs(x+1, alst + [x], blst)
    dfs(x + 1, alst , blst + [x])

def cal(alst, blst):
    asum = 0
    bsum = 0
    for i in range(M): # 0 1
        for j in range(M): # 0 1
            asum += ability_map[alst[i]][alst[j]] # 0 0, 0 1, 1 0, 1 1
            bsum += ability_map[blst[i]][blst[j]]

    return abs(asum - bsum)




dfs(0,[],[])
print(answer)