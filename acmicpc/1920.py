import sys

n = int(sys.stdin.readline().rstrip())
origianllist = list(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(sys.stdin.readline().rstrip())
checklist = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in checklist:
    if i in origianllist:
        print('1')
    else:
        print('0')
