import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for key in list(map(int, input().split())):
    dict[key] = dict.get(key, 0) + 1

m = int(input())

result = []
for key in list(map(int, input().split())):
    result.append(dict.get(key, 0))
    
print(*result)
