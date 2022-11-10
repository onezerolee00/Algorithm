import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

cnt = 0
for A in A_set:
    if(A not in B_set):
        cnt += 1

for B in B_set:
    if(B not in A_set):
        cnt += 1

print(cnt)