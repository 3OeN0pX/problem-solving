def solution(n):
    answer = 0

    for p in range(1, 101):
        if (6*p) % n == 0:
            answer = p
            break

    return answer

