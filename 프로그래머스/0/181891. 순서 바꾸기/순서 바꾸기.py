def solution(num_list, n):
    answer = []
    
    splited_num_list1 = num_list[n:]
    splited_num_list2 = num_list[:n]
    
    answer = splited_num_list1 + splited_num_list2
    
    
    return answer