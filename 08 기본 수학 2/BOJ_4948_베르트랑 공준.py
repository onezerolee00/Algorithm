n = 1

while(n!=0):
    n = int(input())
    if(n==0): # n이 0이면 출력 없이 종료
        break
    isprime_list = [False,False] + [True]*(2*n-1) # 0,1은 소수가 될 수 없으므로 초기값도 False
    cnt = 0

    for i in range(2, 2*n+1):
        if isprime_list[i]:
            if i > n:  # n 초과의 소수
                cnt += 1
            for j in range(2 * i, 2 * n + 1, i):
                isprime_list[j] = False
    print(cnt)

"""
에라토스테네스의 체 활용.
틀린이유 : n 초과의 소수가 아닌 이상의 소수를 구함.
"""