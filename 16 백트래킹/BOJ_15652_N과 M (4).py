N, M = map(int, input().split())
s = []

def dfs(prev):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if(prev <= i):
            s.append(i)
            dfs(i)
            s.pop()

dfs(0)
