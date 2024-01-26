# dic = dict()
#
#
# dic['-'] = []
# dic['-'].append('john')
# dic['-'].append('marry')
#
# print(dic)
#

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referal =["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

parent = dict((zip(enroll, referal)))
# result = [360, 958, 108, 0, 450, 18, 180, 1080]
# dic = dict()
# for x in referal:
#     dic[x] = []
#
# for x, y in zip(referal, enroll) :
#    dic[x].append(y)

print(parent)
