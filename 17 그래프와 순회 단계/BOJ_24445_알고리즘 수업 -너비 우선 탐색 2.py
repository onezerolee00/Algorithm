import sys
input = sys.stdin.readline
from collections import deque

# n: 정점의 수  m: 간선의 수  r: 시작 정점
n, m, r = map(int, input().split())

arr = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

# 양방향 간선
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# 내림차순 적용
for i in arr:
    i.sort(reverse=True)

def bfs(s):
    q = deque() # 다음에 방문할 후보를 담은 q
    answer[r] = 1 # 시작 정점은 방문 순서 1
    cnt = 1 # 방문 순서

    # 시작 정점에서 갈 수 있는 정점 추가
    for i in arr[s]:
        q.append(i)

    while q:
        x = q.popleft()
        if answer[x] == 0: # 방문하지 않았더라면
            cnt += 1 # 방문 순서 +1
            answer[x] = cnt # 해당하는 정점에 방문 순서 대입

            for i in arr[x]: # x 정점에서 갈 수 있는 정점 추가
                q.append(i)

bfs(r)

for i in range(1, n+1):
    print(answer[i])

