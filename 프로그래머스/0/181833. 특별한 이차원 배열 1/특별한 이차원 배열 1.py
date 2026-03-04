def solution(n):
    answer = []
    
    for i in range(n):
        sub_answer = []
        for j in range(n):
            if i == j:
                sub_answer.append(1)
            else:
                sub_answer.append(0)
        answer.append(sub_answer)
    
    return answer