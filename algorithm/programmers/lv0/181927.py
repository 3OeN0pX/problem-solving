def solution(num_list):
    answer = []
    num_list_size = len(num_list)

    last = num_list[num_list_size-1]
    next_to_last = num_list[num_list_size-2]

    if last > next_to_last:
        num_list.append(last - next_to_last)
    else:
        num_list.append(last * 2)

    answer = num_list

    return answer
