import sys
input = sys.stdin.readline

def solve():
    s = input().rstrip('\n')
    n = int(input())
    print(s[n - 1])

if __name__ == "__main__":
    solve()