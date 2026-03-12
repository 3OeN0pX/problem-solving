import sys

input = sys.stdin.readline

t = int(input())

queue = []

for _ in range(t):
    command = input().strip()
    
    if command.startswith('push'):
        cmd, value = command.split()
        queue.append(int(value))
        
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
     
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    
    elif command == "size":
        print(len(queue))
        
    elif command == "empty":
        if queue:
            print(0)
        else:
            print(1)
            
    elif command == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
        
        
        
        