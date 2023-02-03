# import sys
# input = sys.stdin.readline
# from collections import deque
#
# n, m = map(int, input().split())
#
# # visited, graph는 0부터 인덱스 시작하도록 하고
# # 도달해야하는 종점 if문만 잘 처리해주면 될 듯
# visited = [[False]*(m) for _ in range(n)]
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().rstrip())))
#
# break_wall = 1
# cannot_go = False
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# #좌우하상
#
# q = deque()
# q.append((0, 0))
# visited[0][0] = True
# graph[0][0] = 1
#
#
# while q:
#     x, y = q.popleft()
#
#     if x == m-1 and y == n-1:
#         break
#         # print(graph[n-1][m-1])
#
#     for i in range(4): # 상하좌우
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx < 0 or nx >= m or ny < 0 or ny >= n: # 그래프 넘어가면 안됨
#             continue
#
#         if not visited[ny][nx]: # 방문 안한 칸
#             if graph[ny][nx] == 1 and break_wall == 1: # 벽이야 근데 스킬 남음
#                 graph[ny][nx] = graph[y][x] + 1
#                 visited[ny][nx] = True
#                 break_wall = 0
#                 q.append((nx, ny))
#
#             if graph[ny][nx] == 0:
#                 graph[ny][nx] = graph[y][x] + 1
#                 visited[ny][nx] = True
#                 q.append((nx, ny))
#
# if graph[n-1][m-1] == 0:
#     print(-1)
# else:
#     print(graph[n-1][m-1])



import sys
input = sys.stdin.readline
from collections import deque
import copy

n, m = map(int, input().split())

# visited, graph는 0부터 인덱스 시작하도록 하고
# 도달해야하는 종점 if문만 잘 처리해주면 될 듯
# 아니다... 벽 하나마다 결과 append해서 해보자

wall_location = deque()

std_graph = []
for i in range(n):
    row = list(map(int, input().rstrip()))
    std_graph.append(row)
    for j in range(m):
        if row[j] == 1:
            wall_location.append((j, i))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#좌우하상

answer = float('inf')

def bfs(graph):
    global  answer
    q = deque()
    q.append((0, 0))
    visited = [[False] * (m) for _ in range(n)]
    visited[0][0] = True
    graph[0][0] = 1

    while q:
        x, y = q.popleft()

        if x == m - 1 and y == n - 1:
            break
            # print(graph[n-1][m-1])

        for i in range(4):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:  # 그래프 넘어가면 안됨
                continue

            if not visited[ny][nx]:  # 방문 안한 칸
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    visited[ny][nx] = True
                    q.append((nx, ny))

    if graph[n-1][m-1] != 0:
        if answer > graph[n-1][m-1]:
            answer = graph[n-1][m-1]

while wall_location:
    wx, wy = wall_location.popleft()

    # g = std_graph.copy()
    g = copy.deepcopy(std_graph)
    g[wy][wx] = 0

    bfs(g)

if answer == float('inf'):
    print(-1)
else:
    print(answer)



