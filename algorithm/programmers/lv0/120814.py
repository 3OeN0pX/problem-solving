def solution(n):

    pizza_number = n // 7

    if n % 7 != 0:
        pizza_number += 1

    return pizza_number
