import heapq
INF = int(1e9)

# 수빈스: n  동생: k
n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
distance = [INF] * 100001

q = []
distance[n] = 0
heapq.heappush(q, (0, n))
# (시간, 위치)

while q:
    dist, node = heapq.heappop(q)

    for nx in ((node-1, 1), (node+1, 1), (node*2, 0)):
        # nx[0]위치 범위 and 이전 시간이 방금 꺼낸 시간보다 커야함
        if 0<=nx[0]<=100000 and distance[nx[0]] > dist + nx[1]:
            distance[nx[0]] = dist + nx[1]
            heapq.heappush(q, (distance[nx[0]], nx[0]))

print(distance[k])
