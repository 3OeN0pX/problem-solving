def solution(str_list):
    answer = []
    
    l_index = -1
    r_index = -1
    for i in range(len(str_list)):
        target = str_list[i]
        
        if target == "u" or target == "d":
            continue
            
        if target == "l":
            l_index = i
            break
        else:
            r_index = i
            break
        
    if l_index != -1:
        answer = str_list[:l_index]
    
    if r_index != -1:
        answer = str_list[r_index+1:]
        
    
    return answer