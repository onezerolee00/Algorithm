N = int(input())
tmp = N
count = 0
new_number = -1

while(N!=new_number):
    new_number = tmp%10*10 + (tmp//10+tmp%10)%10
    tmp = new_number
    count += 1

print(count)