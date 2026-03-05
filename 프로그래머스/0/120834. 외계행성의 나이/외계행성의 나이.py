def solution(age):
    answer = ''
    
    str_age = str(age)
    
    for target in str_age:
        result = int(target) + ord('a')
        answer += (chr(result))
    
    
    return answer