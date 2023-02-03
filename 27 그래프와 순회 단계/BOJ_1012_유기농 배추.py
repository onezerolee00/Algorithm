import sys
input = sys.stdin.readline
from collections import deque


for _ in range(int(input())):
    m, n, k = map(int, input().split())  # m: 가로길이 n: 세로길이 k: 배추 위치 개수

    graph = [[0 for i in range(m)] for j in range(n)]

    for _ in range(k):
        cx, cy = map(int, input().split())
        graph[cy][cx] = 1

    # 0: (1, 0) 오른쪽,  1: (-1, 0) 왼쪽,  2: (0, -1) 아래쪽,  3: (0, 1) 위쪽
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]


    def bfs(graph, x, y):
        # bfs로 배추 단지를 다 0으로 만들어서 또 탐색되지 않도록 한다.
        q = deque()
        q.append((x, y))
        graph[y][x] = 0

        while q:
            a, b = q.popleft()

            # 상하좌우 탐색 (nx, ny)는 다음 step
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]

                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue

                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((nx, ny))

        return 1


    result = 0

    # 배추 단지의 첫 1을 찾으면 bfs 시작
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result += bfs(graph, j, i)

    print(result)

