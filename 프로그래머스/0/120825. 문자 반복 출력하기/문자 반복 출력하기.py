def solution(my_string, n):
    answer = ''
    
    for ch in my_string:
        for i in range(n):
            answer += ch
    
    
    return answer