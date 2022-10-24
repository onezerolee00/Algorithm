T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if(N%H == 0):
        print(H * 100 + N//H)
    else:
        print(N%H * 100 + N//H + 1)

"""
틀린이유 : N%H == 0의 결우를 고려하지 않음
"""