import sys

def solve():
  input = sys.stdin.readline

  n, k = map(int, input().split())
  rank_list = list(map(int, input().split()))
  grade_list = []

  for rank in rank_list:
    p = (rank * 100) // n

    if p > 96:
      grade_list.append(9)
    elif p > 89:
      grade_list.append(8)
    elif p > 77:
      grade_list.append(7)
    elif p > 60:
      grade_list.append(6)
    elif p > 40:
      grade_list.append(5)
    elif p > 23:
      grade_list.append(4)
    elif p > 11:
      grade_list.append(3)
    elif p > 4:
      grade_list.append(2)
    else:
      grade_list.append(1)

  for i in range(k-1):
    print(f"{grade_list[i]} ", end="")

  print(grade_list[k-1])

if __name__ == "__main__":
  solve()
