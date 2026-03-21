import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for _ in range(m):
    question = input().strip()

    if question.isdigit():
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])