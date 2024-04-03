t=int(input())

for i in range(t):
    h,w,n=map(int,input().split()) #층, 방, 몇번째 손님인지
    
    floor=n%h #층 수
    num=n//h+1 #호 수
    #floor가 0일때를 조절해주어야 함 ex 4%4=0
    #4층 건물, 4개의 방 4번째 손님 => 401
    #따라서 -1을 해주어야 함
    if floor==0:
        floor=h
        num-=1
    print(floor*100+num)