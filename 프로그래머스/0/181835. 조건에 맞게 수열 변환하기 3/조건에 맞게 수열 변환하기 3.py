def solution(arr, k):
    answer = []
    
    if k % 2 == 1:
        for var in arr:
            answer.append(var * k)
    else: 
        for var in arr:
            answer.append(var + k)
    
    return answer