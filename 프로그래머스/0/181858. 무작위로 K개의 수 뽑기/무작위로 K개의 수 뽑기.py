def solution(arr, k):
    answer = []
    seen = set()

    for x in arr:
        if x not in seen:
            seen.add(x)
            answer.append(x)
            if len(answer) == k:
                break

    answer.extend([-1] * (k - len(answer)))
    return answer