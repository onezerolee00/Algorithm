import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())

arr = [[] for _ in range(n+1)]
dfs_visited = [False for _ in range(n+1)]
bfs_visited = [False for _ in range(n+1)]

dfs_result = []
bfs_result = []

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in arr:
    i.sort()

def dfs(s):
    for i in arr[s]:
        if dfs_visited[i] == False:
            dfs_visited[i] = True
            dfs_result.append(i)
            dfs(i)

dfs_visited[r] = True
dfs_result.append(r)
dfs(r)
print(' '.join(map(str, dfs_result)))

def bfs():
    q = deque([])
    bfs_visited[r] = True
    bfs_result.append(r)
    for i in arr[r]:
        q.append(i)

    while q:
        x = q.popleft()
        if bfs_visited[x] == False:
            bfs_visited[x] = True
            bfs_result.append(x)
            for i in arr[x]:
                q.append(i)

    print(' '.join(map(str, bfs_result)))

bfs()
