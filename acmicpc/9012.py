import sys

T = int(sys.stdin.readline().rstrip())
line = []

for i in range(T):
    A = map(str, sys.stdin.readline().rstrip())
    line = list(A)
    count = 0

    for j in range(len(line)):
        if line[j] == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            print("NO")
            break
    
    if count > 0 :
        print("NO")
    elif count == 0:
        print("YES")
    else: pass