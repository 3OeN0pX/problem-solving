import sys

def solve():

  input = sys.stdin.readline

  n = int(input().strip())

  for i in range(1, n+1):
    print(f"Hello World, Judge {i}!")

if __name__ == "__main__":
  solve()
