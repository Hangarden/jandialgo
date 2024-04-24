import heapq

discount_rate = [10, 20, 30, 40]

users = [[40, 10000], [25, 10000]]

emoticons = [7000, 9000]
def discount(emoticon_rate, users, emoticons):
    sums = []
    people = 0
    for i in users:
        x = 0
        for j in range(len(emoticon_rate)):
            if i[0] <= emoticon_rate[j]:
                x += (emoticons[j] * (1 - (emoticon_rate[j] / 100)))
        if x >= i[1]:
            people += 1
            x = 0
        sums.append(x)

    return people, sum(sums)


def back(emoticon_rate, users, emoticons):
    global max_heap
    if len(emoticon_rate) == len(emoticons):
        x, y = discount(emoticon_rate, users, emoticons)
        heapq.heappush(max_heap, (-x, -y))
        return

    for i in discount_rate:
        emoticon_rate.append(i)
        back(emoticon_rate, users, emoticons)
        emoticon_rate.pop()


def solution(users, emoticons):
    global max_heap
    max_heap = []
    emoticon_rate = []
    back(emoticon_rate, users, emoticons)
    return [-(max_heap[0][0]), int(-(max_heap[0][1]))]

print(solution(users, emoticons))