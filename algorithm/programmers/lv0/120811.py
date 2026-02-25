def solution(array):
    answer = 0
    array.sort()

    target_idx = len(array) // 2

    answer = array[target_idx]

    return answer
