def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if 'A' <= ch <= 'Z':
            idx = ord(ch) - ord('A')
        else:
            idx = ord(ch) - ord('a') + 26
        
        answer[idx] += 1
    
    return answer