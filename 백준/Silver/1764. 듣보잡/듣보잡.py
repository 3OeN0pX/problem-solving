import sys

input = sys.stdin.readline

def solve():
    
    n, m = map(int, input().split())
    
    unheard = set()
    for _ in range(n):
        unheard.add(input().strip())
        
    results = []
    for _ in range(m):
        unseen_name = input().strip()
        
        if unseen_name in unheard:
            results.append(unseen_name)
    
    results.sort()
    
    print(len(results))
    for name in results:
        print(name)
        
if __name__ == '__main__':
    solve()