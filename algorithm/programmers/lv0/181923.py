import sys

def solution(arr, queries):
    answer = []

    arr

    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]

        target = -1
        min_var = sys.maxsize
        for idx in range(s, e + 1):
            if arr[idx] > k:
                target = arr[idx]
                if target < min_var:
                    min_var = target
        if target == -1:
            min_var = -1
        answer.append(min_var)

    return answer


