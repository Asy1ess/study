import sys

n, b = map(int, sys.stdin.readline().split( ))
result = []

while n > 0:
  result.insert(0, n % b)
  n = n // b

for i in range(len(result)):
  if result[i] > 9:
    result[i] = chr(result[i]+55) # 아스키코드로 변환하여 출력
  else:
    result[i] = str(result[i]) # 그대로 출력
    

print(''.join(result)) 