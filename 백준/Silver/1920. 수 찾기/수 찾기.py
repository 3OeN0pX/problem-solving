import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

for value in B:
    if value in A:
        print(1)
    else:
        print(0)