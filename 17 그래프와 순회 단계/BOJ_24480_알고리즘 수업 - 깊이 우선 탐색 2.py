import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in arr:
    i.sort(reverse=True)

def dfs(s):
    global cnt
    for i in arr[s]:
        if answer[i] == 0:
            answer[i] = cnt
            cnt += 1
            dfs(i)

global cnt
cnt = 2
answer[R] = 1
dfs(R)

for i in range(1, N+1):
    print(answer[i])