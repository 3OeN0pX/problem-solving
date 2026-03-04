import sys

input = sys.stdin.readline

def solution():
    
    line = input().strip()
    n = int(line)
    
    print(n % 20000303)
    
if __name__ == "__main__":
    solution()