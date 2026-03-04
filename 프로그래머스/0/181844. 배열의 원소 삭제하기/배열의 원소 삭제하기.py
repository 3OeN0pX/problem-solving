def solution(arr, delete_list):
    answer = []
    
    for target in delete_list:
        if target in arr:
            arr.remove(target)
    
    answer = arr
    
    
    return answer