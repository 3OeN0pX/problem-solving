def solution(s1, s2):
    count = 0
    
    for target in s1:
        if target in s2:
            count += 1
    
    return count