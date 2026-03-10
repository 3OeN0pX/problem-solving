def solution(sides):
    sides.sort(reverse=True)
    
    result = sides[0] < sides[1] + sides[2]
    
    if result:
        return 1
    
    
    return 2