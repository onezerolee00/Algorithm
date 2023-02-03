import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

tomatos = []
for _ in range(n):
    tomato = list(map(int, input().split(' ')))
    tomatos.append(tomato)

answer = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 이 부분이 다른 2차원 bfs 문제와는 다르게 푼 핵심 부분이다. 시작점을 여러 개를 찾는다.
def add_tomatos_location(q, t, c):
    for i in range(m):
        for j in range(n):
            if t[j][i] == c:
                q.append((i, j))

    return q

q = deque()
cnt = 1
add_tomatos_location(q, tomatos, cnt)


while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if tomatos[ny][nx] == 0:
            cnt += 1
            tomatos[ny][nx] += tomatos[y][x] + 1
            q.append((nx, ny))


impossible = False

for t in tomatos:
    if 0 in t:
        impossible = True
    if answer < max(t):
        answer = max(t)

if impossible:
    print(-1)
else:
    print(answer - 1)