def solution(numLog):
    answer = ""

    num_log_len = len(numLog)

    for idx in range(num_log_len-1):
        target = numLog[idx+1] - numLog[idx]

        if target == 1:
            answer += "w"
        elif target == -1:
            answer += "s"
        elif target == 10:
            answer += "d"
        else:
            answer += "a"

    return answer
