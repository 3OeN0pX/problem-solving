def solution(price):
    # 기본값을 입력받은 가격으로 설정 (할인 조건에 안 맞을 경우 대비)
    answer = price
    
    if price >= 500000:
        answer = int(price * 0.8)  # 20% 할인
    elif price >= 300000:
        answer = int(price * 0.9)  # 10% 할인
    elif price >= 100000:
        answer = int(price * 0.95) # 5% 할인
    
    return answer