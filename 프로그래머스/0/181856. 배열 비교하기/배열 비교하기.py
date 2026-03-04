def solution(arr1, arr2):
    answer = 0
    
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr2) > len(arr1):
        answer = -1
    else:
        sum_arr1 = 0
        sum_arr2 = 0
        for i in range(len(arr1)):
            sum_arr1 += arr1[i]
            sum_arr2 += arr2[i]
        
        if sum_arr1 > sum_arr2:
            answer = 1
        elif sum_arr2 > sum_arr1:
            answer = -1
        else:
            answer = 0
    
    
    return answer