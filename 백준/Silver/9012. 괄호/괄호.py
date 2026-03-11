# 6
# (())())
# (((()())()

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    line = input().strip()
    count = 0
    valid = True
    
    for target in line:
        if target == "(":
            count += 1
        else:
            count -= 1
        
        if count < 0:
            valid = False
            break

    if count == 0 and valid:
        print("YES")
    else:
        print("NO")