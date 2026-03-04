def solution(arr):
    
    if 2 not in arr:
        return [-1]
    
    start_idx = -1
    end_idx = -1
    
    for i, target in enumerate(arr):
        if target != 2:
            continue
        
        if start_idx == -1:
            start_idx = i
        else:
            end_idx = i
            
    if end_idx == -1:
        return [2]
    
    return arr[start_idx:end_idx+1]