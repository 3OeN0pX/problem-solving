import sys

input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    
    monster_defence = a - (a * b / 100)
    
    if monster_defence < 100:
        print(1)
    else:
        print(0)
    
    
if __name__ == "__main__":
    solution()