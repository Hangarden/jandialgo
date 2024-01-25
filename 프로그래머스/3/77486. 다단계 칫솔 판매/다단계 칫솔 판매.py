import math
def solution(enroll, referral, seller, amount):
    answer = []
    # 우선 추천인을 타고 올라갈 수 있는 dictionary를 만든다
    maps = dict()
    for x,y in zip(enroll, referral):
        maps[x] = y
    
    # 얼마만큼의 수익을 얻었는지 계산할 dict,dict로 구현한 이유는
    # 타고 올라갈 때마다 이름으로 찾기 떄문에 dict로 구현하였음
    total = dict()
    for i in enroll:
        total[i] = 0
        
    # 판매자들만 타고 올라가면 된다
    for i in range(len(seller)):
        money = amount[i] * 100
        name = seller[i]
        
        # 규칙 1,2에 따라서 추천인이 있다면 수익을 나누고 수익이 1보다 작아질때까지 계속하도록
        while money > 0 and name != "-":
          # ➏ 현재 판매자가 받을 금액 계산(10%를 제외한 금액)
          total[name] += money - money // 10
          name = maps[name]
          # ➐ 10%를 제외한 금액 계산
          money //= 10
            
    for i in enroll:
        answer.append(total[i])
        
    print(total)
    
    # print(enroll, referral, seller, amount)
    return answer