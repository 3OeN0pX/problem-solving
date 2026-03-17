import sys

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a = int(input_data[0])
    b = int(input_data[1])
    
    gcd = get_gcd(a, b)
    lcm = (a * b) // gcd
    
    print(gcd)
    print(lcm)

if __name__ == "__main__":
    solve()