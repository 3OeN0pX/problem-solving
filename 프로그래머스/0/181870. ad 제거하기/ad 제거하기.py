def solution(strArr):
    answer = []
    
    for target in strArr:
        if "ad" in target:
            continue
        answer.append(target)
    
    return answer