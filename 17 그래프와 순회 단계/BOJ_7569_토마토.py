import sys
input = sys.stdin.readline
from collections import deque

# m: 상자의 가로 칸  n: 상자의 세로 칸  h: 상자의 수
m, n, h = map(int, input().split())

boxes = []

for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    boxes.append(box)

# 오른쪽 왼쪽 앞 뒤 위 아래
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                q.append((i, j, k))

while q:
    z, y, x = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
            continue

        if boxes[nz][ny][nx] == 0:
            boxes[nz][ny][nx] = boxes[z][y][x] + 1
            q.append((nz, ny, nx))

impossible = False

for box in boxes:
    for tomatos in box:
        if 0 in tomatos:
            impossible = True

answer = -1

if impossible:
    print(-1)
else:
    for box in boxes:
        for tomatos in box:
            if max(tomatos) > answer:
                answer = max(tomatos)
    print(answer-1)
