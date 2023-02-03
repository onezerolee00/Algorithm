import sys
import heapq
# heapq : 원소로 튜플을 입력받으면 튜플의 첫 번째 원소를 기준으로 우선순위 큐를 구성한다.
input = sys.stdin.readline
INF = int(1e9)

# v: 정점의 개수  e: 간선의 개수  k: 시작 정점의 번호
v, e = map(int, input().split())
k = int(input())

graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

# u에서 v로 가는 가중치 w인 간선이 존재
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# (거리, 노드번호)

# 초기값 설정
q = []
heapq.heappush(q, (0, k))
distance[k] = 0

while q:
    # heapq는 우선순위 큐 순서로 되어 있으므로 최단거리가 짧은 노드를 꺼내게 된다.
    dist, node = heapq.heappop(q)
    if distance[node] < dist: # 현 노드의 거리가 방금 꺼낸 노드의 거리보다 작으면 이미 처리된 적 있다는 뜻.
        continue
    for i in graph[node]: # 현 노드에서 갈 수 있는 애들로 거리 계산해서 갱신 (노드, 거리)
        cost = dist + i[1]
        if cost < distance[i[0]]: # 기존의 거리보다 작으면 갱신
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

cnt = 1
for d in distance:
    if cnt == 1:
        cnt += 1
        continue
    if d == INF:
        print('INF')
    else:
        print(d)
#print(distance)
# for i in range(1, v+1):
#     if distance[i] == INF:
#         print('INF')
#     else:
#         print(distance[i])


