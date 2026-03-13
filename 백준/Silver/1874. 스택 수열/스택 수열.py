import sys

input = sys.stdin.readline

n = int(input())
stack = []
result = []
next_num = 1
possible = True

for _ in range(n):
    x = int(input())
    
    while next_num <= x:
        stack.append(next_num)
        result.append("+")
        next_num += 1
    
    if stack and stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break
        
if possible:
    print("\n".join(result))
else:
    print("NO")