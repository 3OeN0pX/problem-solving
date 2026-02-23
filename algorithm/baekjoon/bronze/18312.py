import sys

def solve():
    # 입력 받기
    line = sys.stdin.readline().split()
    
    n, k = map(int, line)
    target = str(k)
    count = 0

    # 00시 00분 00초부터 n시 59분 59초까지 탐색
    for h in range(n + 1):
        # 시(hour)를 두 자리 문자열로 변환 (예: 5 -> "05")
        hh = f"{h:02d}"
        for m in range(60):
            # 분(minute)을 두 자리 문자열로 변환
            mm = f"{m:02d}"
            for s in range(60):
                # 초(second)를 두 자리 문자열로 변환
                ss = f"{s:02d}"

                # 시 분 초 중 하나라도 target(k)이 포함되어 있는지 확인
                if target in hh or target in mm or target in ss:
                    count += 1
    print(count)


if __name__ == "__main__":
    solve()
