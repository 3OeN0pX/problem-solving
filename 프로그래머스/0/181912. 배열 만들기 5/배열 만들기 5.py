def solution(intStrs, k, s, l):
    answer = []
    
    for int_str in intStrs:
        sub_int = int(int_str[s:s+l])
        
        if sub_int > k:
            answer.append(sub_int)
    
    
    return answer