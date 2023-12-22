n, m = map(int, input().split())
board = []
result = []

for i in range(n):
    board.append(input())

for a in range(n-7):
    for b in range(n-7):
        whiteindex = 0
        blackindex = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if board[i][j]!='W':
                        whiteindex += 1
                    else:
                        blackindex += 1
                else:
                    if board[i][j]!='W':
                        blackindex += 1
                    else:
                        whiteindex += 1
        
        result.append(whiteindex)
        result.append(blackindex)
        
print(min(result))