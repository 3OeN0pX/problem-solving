def solution(array, n):
    array.sort()
    
    array.sort(key=lambda x: abs(x - n))
    
    return array[0]