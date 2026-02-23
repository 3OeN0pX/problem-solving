import sys
input = sys.stdin.readline

def calculate_otaku_power(a:int, t:int) -> bool:
    """
    덕후력을 계산해서 반환하는 함수
    """
    p = 10 + 2 *(25 - a + t)
    if p < 0:
        p = 0
    return p

def solve():

    a, t = map(int, input().split())

    otaku_power = calculate_otaku_power(a, t)

    print(otaku_power)

if __name__ == "__main__":
    solve()