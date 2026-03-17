import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    queue = deque(range(1, n + 1))
    result = []
    
    while queue:
        for _ in range(k - 1):
            queue.append(queue.popleft())
        
        result.append(str(queue.popleft()))
    
    print("<" + ", ".join(result) + ">")

if __name__ == "__main__":
    solve()