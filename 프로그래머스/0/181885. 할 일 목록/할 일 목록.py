def solution(todo_list, finished):
    answer = []
    
    for i in range(len(todo_list)):
        if finished[i]:
            continue
        
        answer.append(todo_list[i])
    
    
    return answer