def solution(money):
    answer = []
    
    cup_of_americano = money // 5500
    remain = money % 5500
    answer.append(cup_of_americano)
    answer.append(remain)
    
    return answer