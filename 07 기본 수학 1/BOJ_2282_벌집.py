N = int(input())
n = 0
cnt = 1

while(True):
    if(N == 1):
        print(1)
        break
    if(N <= cnt):
        print(n+1)
        break
    n += 1
    cnt += n * 6

"""
1, 6, 12, 18, 24, ...
1, 7, 19, 37, 61, ...
"""