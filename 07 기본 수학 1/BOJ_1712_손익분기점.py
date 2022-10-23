A, B, C = map(int, input().split())

if(B>=C):
    print(-1)
else:
    print(A//(C-B)+1)

"""
일차 함수 문제이다.
A를 C-B로 나눌 때 ZeroDivisionError를 고려해주어야 한다.
"""