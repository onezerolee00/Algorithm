N = int(input())

candidate = []

a = N // 5
b = (N%5) // 3

c = N // 3
d = (N%3) // 5

n = N
e = 0
while(n>0):
    n -= 3
    e += 1
    if(n%5==0):
        e += n//5
        n -= 5
        candidate.append(e)

if(5*a + 3*b == N):
    candidate.append(a+b)
elif(5*d + 3*c == N):
    candidate.append(c+d)
elif(5*a == N):
    candidate.append(a)
elif(3*c == N):
    candidate.append(c)

if(len(candidate) == 0):
    print(-1)
else:
    print(min(candidate))


"""
- 5킬로그램 봉지로만 배달하는 경우
- 3킬로그램 봉지로만 배달하는 경우
- 5로 나누고 나머지를 3으로 배달하는 경우
- 3를 채우고 나머지를 5로 배달하는 경우
- 불가능한 경우

이렇게 다섯개의 경우의 봉지 수를 고려해 가장 작은 값을 출력하도록 했는데,
모든 경우를 고려하지 않아도 상기 while문 처럼 작성해도 기능이 동작한다.
"""