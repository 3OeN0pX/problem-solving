def solution(my_string, s, e):
    answer = ''
    
    prefix = my_string[:s]
    sub_fix = "".join(reversed(my_string[s:e+1]))
    postfix = my_string[e+1:]
    
    answer = prefix + sub_fix + postfix
    
    return answer