import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            # 갈 수 있는 길이면 이전 step을 더해준다 (cost 계산)
            if graph[ny][nx] == 1:
                graph[ny][nx] += graph[b][a]
                q.append((nx, ny))

            # 도착지점에 도착하면~~~ 여태 누적해서 더해 온 cost를 return!
            if ny == n-1 and nx == m-1:
                return graph[ny][nx]


print(bfs(graph, 0, 0))