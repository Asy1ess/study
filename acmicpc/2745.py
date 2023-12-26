import sys

n, b = sys.stdin.readline().split( )
b = int(b)
result = 0

for i in range(len(n)):
    if n[i].isalpha(): #문자열인지 아닌지 확인
        result += (ord(n[i]) - ord('A') + 10) * pow(b, len(n) - (i+1)) #아스키코드(ord)를 이용하여 값 적용 + 제곱(pow)
    else:
        result +=int(n[i]) * pow(b, len(n)-i-1)
print(result)