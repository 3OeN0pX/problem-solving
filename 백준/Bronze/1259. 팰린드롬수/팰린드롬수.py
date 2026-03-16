import sys

input = sys.stdin.readline

while True:
    number = input().strip()
    
    if number == '0':
        break
    
    prefix = ""
    postfix = ""
    if len(number) % 2 == 0:
        mid_idx = (len(number) // 2)
        
        prefix = number[0:mid_idx]
        postfix = number[mid_idx:]
    else:
        mid_idx = len(number) // 2
    
        prefix = number[0:mid_idx]
        postfix = number[mid_idx+1:]
        
    if prefix == postfix[::-1]:
        print("yes")
    else:
        print("no")
    
    