import sys
input = sys.stdin.readline
from collections import deque

# n: 사다리의 수  m: 뱀의 수
n, m = map(int, input().split())

board = [0] * 101           # 주사위 굴리는 수 저장
visited = [False] * 101     # 방문 여부 저장
go = [0] * 101              # 뱀, 사다리 정보 저장

# 사다리 정보 입력
for _ in range(n):
    x, y = map(int, input().split())
    go[x] = y

# 뱀 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    go[u] = v

# 큐 생성 후 시작 칸 1번 push
q = deque()
q.append(1)

while q:
    x = q.popleft()

    if x == 100:                                # 꺼낸 좌표가 100이면 stop
        print(board[x])
        break

    for i in range(1, 7):                       # 주사위 굴리기~
        nx = x + i

        if nx < 0 or nx > 100:                  # 범위를 넘어가면 안됨
            continue

        if not visited[nx]:                     # 방문하지 않았다면
            if go[nx] != 0:                     # 사다리 or 뱀이 있다면
                nx = go[nx]

            if not visited[nx]:                 # nx가 방문되지 않았다면
                visited[nx] = True
                board[nx] = board[x] + 1
                q.append(nx)

"""
뱀, 사다리가 있는 좌표일 때 nx를 갱신하고 큐를 업데이트 해줘야한다.
처음에는 if 뱀, 사다리가 있는 좌표 else 아닐 때로 해서 답이 안나왔다.
"""