import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

q = deque([])

cnt = 0
visited[1] = True
for i in arr[1]:
    q.append(i)

while q:
    x = q.popleft()

    if visited[x] == False:
        visited[x] = True
        cnt += 1
        for i in arr[x]:
            q.append(i)

print(cnt)