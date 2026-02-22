def solution(my_string, overwrite_string, s):
    start = s
    end = s + len(overwrite_string)
    
    prefix = my_string[:start]  # 덮어쓰기 시작 전
    middle = overwrite_string   # 덮어쓸 부분 
    suffix = my_string[end:]    # 덮어쓰기 끝 이후
    
    answer = prefix + middle + suffix
    
    return answer