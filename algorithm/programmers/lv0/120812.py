def solution(array):
    answer = 0

    mode_list = [0] * 1001

    for num in array:
        mode_list[num] += 1

    max_val = max(mode_list)
    indices = [i for i, x in enumerate(mode_list) if x == max_val]

    if len(indices) > 1:
        answer = -1
    else:
        answer = indices[0]

    return answer
