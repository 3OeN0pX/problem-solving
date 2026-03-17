import sys

input = sys.stdin.readline

def solve():
    
    n = int(input())
    
    points = []
    
    for _ in range(n):
        x, y = map(int, input().split())
        
        point = [x, y]
        points.append(point)
        
    
    points.sort(key=lambda x: (x[0], x[1]))
    
    for point in points:
        print(f"{point[0]} {point[1]}")
    
if __name__ == "__main__":
    solve()