import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# n: 정점의 개수  e: 간선의 개수
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


# graph 그리기 (이동 가능한 정점, 거리)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# v1, v2 입력받기
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        node, dist = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance

start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

# start_1[v1] : 1 -> v1   start_v1[v2] : v1 -> v2   start_v2[n] : v2 -> n
case_1 = start_1[v1] + start_v1[v2] + start_v2[n]
# start_1[v2] : 1 -> v2   start_v2[v1] : v2 -> v1   start_v1[n] : v1 -> n
case_2 = start_1[v2] + start_v2[v1] + start_v1[n]

print(min(case_1, case_2))

"""
case 1) 1 -> v1 -> v2 -> N
case 2) 1 -> v2 -> v1 -> N
"""