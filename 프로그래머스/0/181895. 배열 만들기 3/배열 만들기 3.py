def solution(arr, intervals):
    answer = []
    
    sum_arr1 = arr[intervals[0][0]:intervals[0][1]+1]
    sum_arr2 = arr[intervals[1][0]:intervals[1][1]+1]
    
    answer = sum_arr1 + sum_arr2
    
    return answer