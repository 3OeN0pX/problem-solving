import sys
input = sys.stdin.readline

def solve():
    total = 0
    for _ in range(5):
        total += int(input().strip())
    print(total)

if __name__ == "__main__":
    solve()