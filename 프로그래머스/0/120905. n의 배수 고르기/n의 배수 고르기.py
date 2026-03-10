def solution(n, numlist):
    answer = []
    
    for target in numlist:
        if target % n == 0:
            answer.append(target)
    
    return answer