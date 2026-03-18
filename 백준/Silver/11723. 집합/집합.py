import sys

input = sys.stdin.readline

def solve():
    line1 = input().strip()
    if not line1: return
    M = int(line1)
    
    S = set() 
    
    for _ in range(M):
        line = input().strip()
        if not line: continue
        
        if line == 'all':
            S = set(range(1, 21))
        elif line == 'empty':
            S = set() 
        else:
            command, value = line.split()
            value = int(value)
            
            if command == 'add':
                S.add(value)
            elif command == 'remove':
                S.discard(value)
            elif command == 'check':
                print(1 if value in S else 0)
            elif command == 'toggle':
                if value in S:
                    S.discard(value)
                else:
                    S.add(value)

if __name__ == '__main__':
    solve()