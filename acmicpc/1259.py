import sys

while True:
    num = list(sys.stdin.readline().rstrip())
    rev = num[::-1]

    if num[0] == '0':
        break
    
    if num == rev:
        print('yes')
    else:
        print('no')