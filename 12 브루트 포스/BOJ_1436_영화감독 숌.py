N = int(input())

devil = 1
num = 666

while(N>=devil):
    if(N==devil):
        break
    num += 1
    if('666' in str(num)):
        devil += 1

print(num)