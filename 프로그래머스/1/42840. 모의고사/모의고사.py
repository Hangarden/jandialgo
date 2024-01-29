def solution(answers):
    answer = [0]
    # print(answers)
    student1 = [1, 2, 3, 4, 5] * 2001
    student2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1001
    # print(student1)
    score1, score2, score3 = 0,0,0
    
    for i in range(len(answers)): # 5 0 1 2 3 4
        if answers[i] == student1[i]:
            score1 += 1
    for i in range(len(answers)): # 5 0 1 2 3 4
        if answers[i] == student2[i]:
            score2 += 1
    for i in range(len(answers)): # 5 0 1 2 3 4
        if answers[i] == student3[i]:
            score3 += 1

    answer.append(score1)
    answer.append(score2)
    answer.append(score3)
          
    answer_s =[]
    for i in range(len(answer)):
        if answer[i] == max(answer):
            answer_s.append(i)              
    return answer_s