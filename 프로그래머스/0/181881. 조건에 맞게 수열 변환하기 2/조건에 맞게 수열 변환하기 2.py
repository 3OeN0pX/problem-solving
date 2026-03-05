def solution(arr):
    
    before_arr = []
    after_arr = arr
    count = -1
    while before_arr != after_arr:
        before_arr = after_arr[:]
        
        for i in range(len(after_arr)):
            num = after_arr[i]
            if num >= 50 and num % 2 == 0:
                num = num // 2
            elif num < 50 and num % 2 == 1:
                num = (num * 2) + 1
            
            after_arr[i] = num
        
        count += 1

    return count