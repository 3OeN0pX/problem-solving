def solution(numbers):
    answer = 0

    numbers_len = len(numbers)
    sum = 0
    for number in numbers:
        sum += number

    answer = sum / numbers_len

    return answer
