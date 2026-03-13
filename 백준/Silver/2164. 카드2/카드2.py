# 제일 위의 카드 버린다.
# 제일 위에 있는 카드를 제일 아래로 옮긴다.

from collections import deque

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    
else:
    queue = deque(range(1, n+1))
    
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    
    print(queue[0])
    