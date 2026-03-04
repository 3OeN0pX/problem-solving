def solution(str_list, ex):
    answer = ''
    
    for target in str_list:
        
        if ex in target:
            continue
        
        answer += target
        

    return answer