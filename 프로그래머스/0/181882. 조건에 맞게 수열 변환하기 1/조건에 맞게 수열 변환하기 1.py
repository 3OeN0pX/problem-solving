def solution(arr):
    answer = []
    
    for target in arr:
        if target >= 50 and target % 2 == 0:
            answer.append(target // 2)
        elif target < 50 and target % 2 == 1:
            answer.append(target * 2)
        else:
            answer.append(target)
    
    
    
    return answer