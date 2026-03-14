def solution(order):
    
    count = 0
    target = {'3', '6', '9'}
    
    for ch in str(order):
        if ch in target:
            count += 1
    
    return count