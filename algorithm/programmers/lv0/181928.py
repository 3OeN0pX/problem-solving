def solution(num_list):
    answer = 0
    hol = []
    jjak = []

    for num in num_list:
        num_str = str(num)
        if num % 2 == 0:
            jjak.append(num_str)
        else:
            hol.append(num_str)

    attached_hol = int("".join(hol))
    attached_jjak = int("".join(jjak))

    answer = attached_hol + attached_jjak

    return answer
