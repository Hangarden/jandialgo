def solution(phone_book):
    answer = True
    
    Hash_map = {}
    
    for number in phone_book:
        if number not in Hash_map:
            Hash_map[number] = 1
    
    
    for nums in phone_book:
        arr = ""
        for x in nums:
            arr += x
            if ( arr in Hash_map ) and ( arr != nums ):
                answer = False
                return answer
            
    answer = True
    return answer