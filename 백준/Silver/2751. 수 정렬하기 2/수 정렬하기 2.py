import sys

input = sys.stdin.readline

def solve():
    
    n = int(input())
    
    sorted_arr = []
    for _ in range(n):
        sorted_arr.append(int(input()))
        
    sorted_arr.sort()
    
    for num in sorted_arr:
        print(num)
        
if __name__ == '__main__':
    solve()