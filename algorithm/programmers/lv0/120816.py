def solution(slice, n):
    answer = 0

    for p in range(1, 1001):
        if p * slice >= n:
            answer = p
            break


    return answer
