import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True


n = int(input())
num_list = list(map(int, input().split()))
count = 0

for num in num_list:
    if is_prime(num):
        count+=1

print(count)
