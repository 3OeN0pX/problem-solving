import sys

input = sys.stdin.readline

t = int(input())
out = []

for _ in range(t):
    n = int(input())
    if n == 1:
        out.append("#")
    else:
        lines = ["#" * n]
        mid = "#" + "J" * (n - 2) + "#"
        for _ in range(n - 2):
            lines.append(mid)
        lines.append("#" * n)
        out.append("\n".join(lines))

sys.stdout.write("\n\n".join(out))