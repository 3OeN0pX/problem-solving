def solution(picture, k):
    answer = []
    
    for row in picture:
        expanded_row = ''.join(ch * k for ch in row)  # 가로 k배 확대
        for _ in range(k):                            # 세로 k배 확대
            answer.append(expanded_row)
    
    return answer