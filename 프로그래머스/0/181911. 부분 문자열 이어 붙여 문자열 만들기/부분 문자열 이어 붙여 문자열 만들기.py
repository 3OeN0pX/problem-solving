def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(my_strings)):
        target_string = my_strings[i]
        s = parts[i][0]
        e = parts[i][1]
        
        sub_string = target_string[s:e+1]
        
        answer += sub_string
    
    
    return answer