def solution(binomial):
    answer = 0
    
    splited_binomial = binomial.split()
    
    a = int(splited_binomial[0])
    b = int(splited_binomial[2])
    op = splited_binomial[1]
    
    if op == "+":
        answer = a+b
    elif op == "-":
        answer = a-b
    else:
        answer = a * b
    
    
    
    return answer