def solution(a, d, included):
    answer = 0

    for idx, target in enumerate(included):
        if target:
            answer += ((idx * d) + a)

    return answer
