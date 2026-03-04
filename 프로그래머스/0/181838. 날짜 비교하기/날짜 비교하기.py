def solution(date1, date2):
    answer = 0
    
    if date2[0] >= date1[0]:
        if date2[1] >= date1[1]:
            if date2[1] == date1[1] and date2[2] > date1[2]:
                answer = 1
            elif date2[1] > date1[1]:
                answer = 1
                
        
    return answer