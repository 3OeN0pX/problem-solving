def solution(my_string, queries):
    answer = ''
    
    for query in queries:
        s = query[0]
        e = query[1] + 1

        prefix = my_string[:s]
        reversed_sub_str = "".join(reversed(my_string[s:e]))
        postfix = my_string[e:]
        
        my_string = prefix + reversed_sub_str + postfix
        
    answer = my_string
    
    return answer