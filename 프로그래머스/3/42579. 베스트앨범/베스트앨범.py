def solution(genres, plays):
    answer = []
    genre_set = set(genres)
    total = [(idx, x,y) for idx,(x,y) in enumerate(zip(genres, plays))]
    # print(total) 
    
    
    # for x,y in 
    
    # print(genre_set)
    
    #장르 순위를 결정할 dict
    total_chart = {}
    # 장르별 플레이리스트를 결정할 dict
    genre_rank = {}
    for idx, genre, plays in total:
        if genre not in total_chart:
            total_chart[genre] = plays
        else:
            total_chart[genre] += plays
            
        if genre not in genre_rank:
            genre_rank[genre] = [(plays, idx)]
        else:
            genre_rank[genre].append((plays, idx))
    # print(total_chart)
    # print(genre_rank)
                                     
    # total_chart = sorted(total_chart, reverse = True)
    
    total_chart = sorted(total_chart.items(), key=lambda x:x[1],reverse = True)
#     print(total_chart)
    
#     genre_rank = sorted(genre_rank[i[0]], key = lambda x : (-x[0], x[1]))[:2]
#     print(genre_rank)
    for i in total_chart:
        for x in sorted(genre_rank[i[0]], key = lambda x : (-x[0], x[1]))[:2]:
            answer.append(x[1])
            
    return answer