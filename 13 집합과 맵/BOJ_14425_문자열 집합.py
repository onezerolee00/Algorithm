import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S_dict = {}
for i in range(N):
    S_dict[input().strip()] = 0

cnt = 0
for j in range(M):
    if(input().strip() in S_dict):
        cnt += 1

print(cnt)