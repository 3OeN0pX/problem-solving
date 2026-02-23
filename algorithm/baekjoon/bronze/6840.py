import sys
input = sys.stdin.readline

def solve():
    answer = 0
    weights = []
    for _ in range(3):
        weights.append(int(input().strip()))
    
    weights.sort()
    answer = weights[1]
    print(answer)

if __name__ == "__main__":
    solve()