import sys

N = int(sys.stdin.readline().rstrip())
A = {i: 1 for i in map(int, sys.stdin.readline().rstrip().split())}
M = int(sys.stdin.readline().rstrip())

for i in list(map(int, sys.stdin.readline().rstrip().split())):
    print(A.get(i, 0))