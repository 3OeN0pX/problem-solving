def solution(num_list):
    answer = 0
    gop = 1
    hap = 0

    for num in num_list:
        gop *= num
        hap += num

    if gop > hap**2:
        answer = 0
    else:
        answer = 1

    return answer
