def solution(participant, completion):
    answer = ''
    d = {}
    
    for target in participant:
        if d.get(target):
            d[target] += 1
        else:
            d[target] = 1
    
    for target in completion:
        d[target] -= 1
        
    for key, value in d.items():
        if value == 1:
            answer = key
            break
            
    
    return answer