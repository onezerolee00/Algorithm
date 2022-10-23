X = int(input())
n = 0

while(True):
    n += 1
    if(X <= (n*(n+1))//2):
        break

offset = X - (n*(n-1))//2

if(n%2 == 1):
    print(n-offset+1, '/', offset, sep='')
else:
    print(offset, '/', n - offset + 1, sep='')

"""
각 단계의 요소의 수는 1씩 늘어난다.
입력받은 X로부터 단계 n과 단계 n에서 offset을 구한다.
n이 홀수이면 분자가 n부터 1까지 오름차순, 분모가 1부터 n까지 내림차순이다.
n이 짝수이면 분자가 1부터 n까지 내림차순, 분자가 n부터 1까지 오름차순이다.

1단계 : 1/1
2단계 : 1/2 2/1
3단계 : 3/1 2/2 1/3
4단계 : 1/4 2/3 3/2 4/1
...
"""