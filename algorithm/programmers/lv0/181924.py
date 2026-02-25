def solution(arr, queries):
    answer = []

    for query in queries:
        idx1 = query[0]
        idx2 = query[1]

        temp = arr[idx2]
        arr[idx2] = arr[idx1]
        arr[idx1] = temp

    answer = arr

    return answer
