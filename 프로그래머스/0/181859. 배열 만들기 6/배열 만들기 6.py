def solution(arr):
    stk = []
    
    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
            continue
        
        if stk[-1] == arr[i]:
            stk = stk[:len(stk)-1]
            continue
        
        if stk[-1] != arr[i]:
            stk.append(arr[i])
            continue
            
    if not stk:
        return [-1]
    
    return stk