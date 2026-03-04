import sys

input = sys.stdin.readline

def solution():
    
    n = int(input().strip())
    
    min_x_y = [1001, 1001]
    for i in range(n):
        x, y = map(int, input().split())
        
        if y < min_x_y[1]:
            min_x_y = [x, y]
    
    print(f"{min_x_y[0]} {min_x_y[1]}")
            

if __name__ == "__main__":
    solution()