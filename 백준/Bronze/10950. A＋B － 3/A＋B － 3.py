import sys
input = sys.stdin.readline

def solution():
    # 첫 줄에서 테스트 케이스 개수 n을 읽음
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
        
        for i in range(n):
            # 오타 수정: intpu -> input
            a, b = map(int, input().split())
            print(a + b)
    except ValueError:
        pass
        
if __name__ == "__main__":
    solution()