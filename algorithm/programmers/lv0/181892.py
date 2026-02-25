def solution(num_list, n):
    answer = []
    num_list_len = len(num_list)

    for i in range(n-1, num_list_len):
        answer.append(num_list[i])

    return answer
