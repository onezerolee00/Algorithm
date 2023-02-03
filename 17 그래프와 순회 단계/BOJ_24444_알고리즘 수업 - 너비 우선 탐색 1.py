import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in arr:
    i.sort()

q = deque([])
for i in arr[R]:
    q.append(i)

answer[R] = 1
cnt = 1

while q:
    x = q.popleft()
    if answer[x] == 0:
        cnt += 1
        answer[x] = cnt
        for i in arr[x]:
            q.append(i)

for i in range(1, N+1):
    print(answer[i])