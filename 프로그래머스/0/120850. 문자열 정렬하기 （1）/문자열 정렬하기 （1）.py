def solution(my_string):
    answer = []
    
    a = "3"
    
    for target in my_string:
        if target >= "0" and target <= "9":
            answer.append(int(target))
    
    answer.sort()
    
    return answer