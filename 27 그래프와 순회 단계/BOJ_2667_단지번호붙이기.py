import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0 # 방문한 곳을 또 방문하지 않도록..
    cnt = 1 # 단지 내 집의 수

    while q:
        a, b = q.popleft()

        for i in range(4): # 1: 왼쪽 2: 오른쪽 3:아래쪽 4: 위쪽
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 만약 그래프를 넘어가면 pass
                continue

            if graph[nx][ny] == 1: # 단지 시작 장소 찾았다
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt



result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

print(len(result))
for i in sorted(result):
    print(i)
