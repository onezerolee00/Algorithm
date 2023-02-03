import sys
input = sys.stdin.readline
from collections import deque

# v: 정점의 개수  e: 간선의 개수
v, e = map(int, input().split())

"""
양방향 간선으로 설정한 담에
음,, 음,,, 다음 위치를 다 현재 색이랑 다른 색으로 색칠하는거
그리고 검사를 해 만약 현재 색이랑 다음 위치의 색이 같이면 아닌 거죵
아닌 듯
음 단방향 arr 양방향 arr 둘 다 만들어서
단방향은 색칠에 쓰고 양방향은 검사에 쓰는 거얌 어때
"""
arr = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
color_arr = [0 for _ in range(v+1)]

for _ in range(e):
    u, v = map(int, input().split(' '))
    arr[u].append(v)
    arr[v].append(u)

q = deque()
q.append(1)

print(arr)

cnt = 0
# 색칠
while(q):
    print(q)
    x = q.popleft()

    if cnt == v:
        break

    for i in arr[x]:
        if not visited[i]:
            nx = i
            if color_arr[x] == 0:
                color_arr[nx] == 1
                cnt += 1
            elif color_arr[x] == 1:
                color_arr[nx] == 0
                cnt += 1
            q.append(nx)

print(color_arr)