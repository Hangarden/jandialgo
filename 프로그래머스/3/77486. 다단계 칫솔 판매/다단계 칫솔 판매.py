def solution(enroll, referral, seller, amount):
    referral_dict ={}

    for x, y in zip(enroll, referral):
        referral_dict[x] = y
    profit_dict = {}
    for x in enroll:
        profit_dict[x] = 0
    # referal_dict생성완료
    # print(referral_dict)
    # money_dict 생성 완료
    # print(profit_dict)
    
    for name, x in zip(seller, amount):
        profit = 100 * x
        seller_name = name
        while seller_name != '-' and profit >= 1:
            profit_dict[seller_name] += (profit - (profit//10))
            profit //= 10
            seller_name = referral_dict[seller_name] 
    
    answer = []    
    for i in enroll:
        answer.append(profit_dict[i])
    
    return answer