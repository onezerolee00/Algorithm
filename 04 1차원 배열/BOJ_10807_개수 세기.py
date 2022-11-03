N = int(input())
array = list(map(int, input().split()))
v = int(input())
cnt = 0

for a in array:
    if(a == v):
        cnt += 1

print(cnt)