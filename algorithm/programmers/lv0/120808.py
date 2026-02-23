import math

def solution(numer1, denom1, numer2, denom2):
    # 1. 분자, 분모 계산 (통분)
    total_numer = numer1 * denom2 + numer2 * denom1
    total_denom = denom1 * denom2
    
    # 2. 최대공약수(GCD) 구하기
    common = math.gcd(total_numer, total_denom)
    
    # 3. 최대공약수로 나누어 약분하기 
    return [total_numer / common, total_denom / common]