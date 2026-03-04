def solution(num_list):
    answer = 0
    
    sum_jjack = 0
    sum_hol = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum_hol += num_list[i]
            continue
        sum_jjack += num_list[i]
    
    if sum_jjack > sum_hol:
        answer = sum_jjack
    else:
        answer = sum_hol
    
    return answer