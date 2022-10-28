M, N = map(int, input().split())
isprime_list = [False,False] + [True]*(N-1) # 0,1은 소수가 될 수 없으므로 초기값도 False

for i in range(2, N+1):
  if isprime_list[i]:
      if i>=M: # M 이상의 소수
          print(i)
      for j in range(2*i, N+1, i): # 소수의 배수는 소수가 아니므로 False
          isprime_list[j] = False

"""
시간초과를 피하기 위해서는 『에라토스테네스의 체』라는 소수를 구하는 방법을 사용해야한다.
에라토스테네스의 체란 합성수를 지워 소수를 찾는 방법으로, 가장 작은 소수를 찾고 그 소수는 지우지 않고 그 소수의 배수를 지우는 방식이다.
"""