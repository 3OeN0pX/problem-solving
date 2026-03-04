def solution(a, b):
    answer = 0
    
    a_remain = a % 2
    b_remain = b % 2
    sum_remain = a_remain + b_remain
    
    if sum_remain == 2:
        answer = a**2 + b**2
    elif sum_remain == 1:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    
    
    
    return answer