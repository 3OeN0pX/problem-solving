import sys

input = sys.stdin.readline

t = int(input())

stack = []

for _ in range(t):
    command = input().strip()

    if command.startswith("push"):
        cmd, value = command.split()
        stack.append(int(value))

    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)