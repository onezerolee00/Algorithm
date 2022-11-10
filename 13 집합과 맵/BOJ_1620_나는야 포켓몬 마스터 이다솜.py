import sys
input = sys.stdin.readline

N, M = map(int, input().split())

PocketMon_dict = {}
for i in range(1, N+1):
    x = input().rstrip()
    PocketMon_dict[x] = i
    PocketMon_dict[i] = x

for j in range(M):
    x = input().rstrip()
    if(x.isdigit()):
        print(PocketMon_dict[int(x)])
    else:
        print(PocketMon_dict[x])

"""
key가 string인 경우와 integer인 경우를 모두 dictionary에 저장하는 것이 핵심.
"""