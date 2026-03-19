import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    
    times = list(map(int, input().split()))
    times.sort()
    total = 0
    current_sum = 0
    
    for time in times:
        current_sum += time
        total += current_sum
        
    print(total)
    
if __name__ == '__main__':
    solve()