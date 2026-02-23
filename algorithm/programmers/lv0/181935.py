def solution(n):
    answer = 0
    is_even = False
    
    if n % 2 == 1:
        is_even = True
    
    if is_even:
        for num in range(n+1):
            if num % 2 == 1:
                answer += num
    else:
        for num in range(n+1):
            if num % 2 == 0:
                answer += (num**2)
    
    return answer