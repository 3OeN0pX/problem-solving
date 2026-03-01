def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        converted = str(i)
        
        check = True
        for ch in converted:
            if ch == "0" or ch == "5":
                continue
            else:
                check = False
                break
        
        if check:
            answer.append(i)
    
    if not answer:
        answer.append(-1)
    
    return answer