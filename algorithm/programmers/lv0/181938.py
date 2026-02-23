def solution(a, b):
    
    sum_ab = int(str(a) + str(b))
    calculated = 2 * a * b
    
    answer = 0
    if sum_ab > calculated:
        answer = sum_ab
    else:
        answer = calculated
    
    return answer