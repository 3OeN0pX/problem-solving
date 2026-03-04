def solution(my_string):
    answer = []
    
    for i in range(len(my_string)):
        postfix = my_string[i:]
        answer.append(postfix)
        
    answer.sort()
    
    return answer