from collections import deque
import sys
input = sys.stdin.readline

# n: 정점의 개수  m: 간선의 개수
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        nx = q.popleft()

        for i in arr[nx]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        answer += 1
        bfs(i)

print(answer)