def solution(arr):
    
    arr_len = len(arr)
    
    target = 1 << (arr_len-1).bit_length()
    
    for i in range(arr_len, target):
        arr.append(0)
    
    
    
    return arr