def solution(n_str):
    answer = ''
    
    find_idx = -1
    for i in range(len(n_str)):
        if n_str[i] != "0":
            break
        
        find_idx = i
        
    if find_idx == -1:
        answer = n_str
    else: 
        answer = n_str[find_idx+1:]
    
    
    
    return answer