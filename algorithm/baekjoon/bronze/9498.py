import sys

def solve():
  input = sys.stdin.readline

  score = int(input().strip())

  if score >= 90:
    print("A")
  elif score >= 80:
    print("B")
  elif score >= 70:
    print("C")
  elif score >= 60:
    print("D")
  else:
    print("F")

if __name__ == "__main__":
  solve()
