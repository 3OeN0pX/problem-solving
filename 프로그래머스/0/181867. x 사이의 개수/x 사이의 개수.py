def solution(myString):
    answer = []
    
    len = 0
    for target in myString:
        if target == "x":
            answer.append(len)
            len = 0
            continue
        
        len += 1
    
    answer.append(len)
    
    
    return answer