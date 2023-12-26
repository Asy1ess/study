import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
result = []

for a in range(n-7):
    for b in range(m-7):
        whiteindex = 0
        blackindex = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        whiteindex += 1
                    if board[i][j] != 'B':
                        blackindex += 1
                else:
                    if board[i][j] != 'B':
                        whiteindex += 1
                    if board[i][j] != 'W':
                        blackindex += 1
        result.append(min(whiteindex, blackindex))

print(min(result))