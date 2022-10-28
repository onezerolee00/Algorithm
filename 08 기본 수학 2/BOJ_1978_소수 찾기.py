def is_prime(num):
    if(num == 1):
        return False
    for i in range(2, num):
        if(num%i == 0):
            return False
    return True

N = int(input())
number_list = list(map(int, input().split()))
cnt = 0

for number in number_list:
    if(is_prime(number)):
        cnt += 1

print(cnt)