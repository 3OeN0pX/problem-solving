import sys

input = sys.stdin.readline

def solve():
    
    n = int(input())
    
    arr = []
    for _ in range(n):
        target = []
        age, name = input().split()
        age = int(age)
        
        target.append(age)
        target.append(name)
        
        arr.append(target)
        
    arr.sort(key=lambda x: x[0])
    
    for member in arr:
        print(f"{member[0]} {member[1]}")
        
if __name__ == "__main__":
    solve()