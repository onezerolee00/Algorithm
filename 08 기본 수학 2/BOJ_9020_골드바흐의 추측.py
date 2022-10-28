def isPrime(n):
    isprime_list = [False, False] + [True]*(n-1)

    for i in range(2, n+1):
        if isprime_list[i]:
            for j in range(2*i, n+1, i):
                isprime_list[j] = False
    return isprime_list

isprime_list = isPrime(10000)

for i in range(int(input())):
    n = int(input())
    for j in range(n//2, 0, -1):
        if(isprime_list[j] and isprime_list[n-j]):
            print(j, n-j)
            break

"""
시간초과 1: 
각 n마다 2부터 n까지의 소수를 찾고 n이 될 수 있는 두 소수의 조합을 리스트에 올렸다. 
그리고 그 중에서 차이가 가장 적은 조합을 선택했다. 시간초과 발생.

시간초과 2: 
시간초과 1를 피하기 위해서 n의 절반에서 1, -1씩 더한 값들이 소수인지 확인하고 출력하도록 했다.
소수인 지 확인할 때마다 에라토스테네스의 체에서 사용되는 리스트를 생성하므로 시간초과 발생.
따라서, 10000까지의 수가 소수인 지 알 수 있는 리스트를 미리 생성하여 활용한다. (4<=n<=10000)
"""

# T = int(input())
#
# for t in range(T):
#     n = int(input())
#
#     isprime_list = [False, False] + [True]*(n-1)
#     primes = []
#
#     for i in range(2, n+1):
#         if isprime_list[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 isprime_list[j] = False
#
#     partition = []
#
#     for i in range(len(primes)):
#         for j in range(len(primes)):
#             if(n == primes[i]+primes[j]):
#                 partition.append(primes[i])
#                 partition.append(primes[j])
#
#     print(partition)
#     if(len(partition)//2%2==0):
#         print(partition[len(partition)//2-2], partition[len(partition)//2-1])
#     else:
#         print(partition[len(partition)//2-1], partition[len(partition)//2])
#

# T = int(input())
#
# for t in range(T):
#     n = int(input())
#
#     isprime_list = [False, False] + [True]*(n-1)
#     primes = []
#
#     for i in range(2, n+1):
#         if isprime_list[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 isprime_list[j] = False
#
#     repeat = True
#
#     for i in range(len(primes)//2, 0, -1):
#         if not repeat:
#             break
#         for j in range(len(primes)//2+1, len(primes)):
#             if (n == primes[i-1] + primes[j-1]):
#                 print(primes[i-1], primes[j-1])
#                 repeat = False
#                 break
#             if (n == primes[j-1] + primes[j-1]):
#                 print(primes[j-1], primes[j-1])
#                 repeat = False
#                 break