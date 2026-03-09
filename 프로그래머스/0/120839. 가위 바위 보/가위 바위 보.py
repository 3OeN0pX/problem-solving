def solution(rsp):
    answer = ''
    
    for target in rsp:
        if target == "0":
            answer += "5"
        elif target == "2":
            answer += "0"
        else:
            answer += "2"
    
    return answer