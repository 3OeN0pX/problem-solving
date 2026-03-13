def solution(my_string):
    answer = 0
    
    a = "3"
    
    for target in my_string:
        if target >= "0" and target <= "9":
            answer += int(target)
    
    return answer