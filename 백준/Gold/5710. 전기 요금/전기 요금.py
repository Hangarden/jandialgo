def transfer_watt(a):
    if a  <= 200:
        return a / 2
    elif a <= 29900:
        return ( (a - 200) / 3 ) + 100
    elif a <= 4979900:
        return ( (a - 29900) / 5 ) + 10000
    else:
        return ( (a - 4979900) / 7) + 1000000

def transfer_price(watt):
    price = [2,3,5,7]
    if watt <= 100:
        return watt * 2
    elif watt <= 10000:
        return 200 + (watt - 100) * 3
    elif watt <= 1000000:
        return 29900 + (watt - 10000) * 5
    else:
        return 4979900 + (watt - 1000000) * 7


while True:
    a, b= map(int, input().split())
    if a == b == 0:
        break
    else:
        end = transfer_watt(a)
        # print(end)
        total = transfer_watt(a)
        start = 0

        while start <= end:
            mid = int((start + end) / 2)
            other_use = total - mid

            diff = abs(transfer_price(mid) - transfer_price(other_use))
            if diff == b:
                print(transfer_price(mid))
                break
                # 차이가 b보다 크다면 두 요금사이 격차가 크니 줄여야 한다 end를 줄여야 한다.
            elif diff > b:
                start = mid + 1
            elif diff < b:
                end = mid - 1


