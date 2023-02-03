import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(int(input())): # 테스트 케이스
    l = int(input()) # 체스판의 한 변의 길이
    board = [[0 for _ in range(l)] for _ in range(l)]

    a, b = map(int, input().split()) # 나이트가 현재 있는 칸
    ax, ay = map(int, input().split()) # 나이트가 이동하려고 하는 칸 (목적지)

    q = deque()
    q.append((a, b))
    board[b][a] = 1

    while q:
        x, y = q.popleft() # 현재 칸

        if x == ax and y == ay:
            print(board[y][x] - 1)

        for i in range(8): # 다음 이동 칸
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= l or ny < 0 or ny >= l: # 범위를 넘는 다면 pass
                continue

            if board[ny][nx] == 0: # 방문하지 않았다면
                q.append((nx, ny))
                board[ny][nx] = board[y][x] + 1


