import sys

input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)

new_avg = (sum(scores) * 100) / (M * N)

print(new_avg)