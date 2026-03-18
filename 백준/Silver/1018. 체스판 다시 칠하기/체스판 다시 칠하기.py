import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    
    min_paint = float('inf')

    for i in range(n - 7):
        for j in range(m - 7):
            draw1 = 0
            draw2 = 0
            
            for row in range(i, i + 8):
                for col in range(j, j + 8):
                    if (row + col) % 2 == 0:
                        if board[row][col] != 'W':
                            draw1 += 1
                        if board[row][col] != 'B':
                            draw2 += 1
                    else:
                        if board[row][col] != 'B':
                            draw1 += 1
                        if board[row][col] != 'W':
                            draw2 += 1
            
            min_paint = min(min_paint, draw1, draw2)

    print(min_paint)

solve()