def solution(array, height):
    
    array.sort(reverse=True)
    
    count = 0
    for target in array:
        if target > height:
            count += 1
            continue
        
        break
    
    return count