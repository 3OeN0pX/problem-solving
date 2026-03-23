# n = 1 일때 경우의 수는 1
# n = 2 일때 경우의 수는 2
# 점화식: f(n) = f(n-1) + f(n-2)

import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    n_arr = [0] * (n + 1)
    n_arr[1] = 1
    n_arr[2] = 2

    for i in range(3, n + 1):
        n_arr[i] = (n_arr[i - 1] + n_arr[i - 2]) % 10007

    print(n_arr[n])