def solution(myString, pat):
    answer = 0
    
    changed_myString = ''
    
    for ch in myString:
        if ch == 'A':
            changed_myString += 'B'
        else:
            changed_myString += 'A'
            
    if pat in changed_myString:
        answer = 1
    
    return answer