def solution(a, b):
    
    sum_first = int(str(a) + str(b))
    sum_second = int(str(b) + str(a))
    
    answer = 0
    if sum_second > sum_first:
        answer = sum_second
    else:
        answer = sum_first
    
    return answer