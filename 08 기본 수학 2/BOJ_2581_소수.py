def is_prime(num):
    if(num == 1):
        return False
    for i in range(2, num):
        if(num%i == 0):
            return False
    return True

M = int(input())
N = int(input())
prime_list = []

for i in range(M, N+1):
    if(is_prime(i)):
        prime_list.append(i)

if(len(prime_list) == 0):
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
