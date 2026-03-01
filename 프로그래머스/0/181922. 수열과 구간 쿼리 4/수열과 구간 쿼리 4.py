# S <= i <= e 인 모든 i에 대해
# i가 K의 배수이면 arr[i]에 1을 더한다

def solution(arr, queries):
    answer = []
    
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        for i in range(s, e+1):
            if i % k == 0:
                arr[i] += 1
    
    answer = arr
    
    return answer