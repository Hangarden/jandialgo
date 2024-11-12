

str = list(input().split())
# print(str)

default = str[0]
priority = {'&' : 5, '[]' : 3, '*' : 1}


for i in str[1:]:
    strs = default
    word = ""
    alpha = ""
    for x in i[::-1]:
        if x == "&" or x == "[" or x == "]" or x == "*":
            word += x
        elif x.isalpha():
            alpha += x
    alpha = alpha[::-1]
    # print(word)
    word = word.replace("][", "[]")
    strs += word + " " + alpha + ";"
    print(strs)