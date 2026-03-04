import sys

n = int(sys.stdin.readline().strip())

if n % 2 == 0:
    sys.stdout.write("I LOVE CBNU")
else:
    t = n // 2
    out = []
    out.append("*" * n)
    out.append(" " * (n - t - 1) + "*")
    for i in range(t):
        out.append(" " * (t - i - 1) + "*" + " " * (2 * i + 1) + "*")
    sys.stdout.write("\n".join(out))