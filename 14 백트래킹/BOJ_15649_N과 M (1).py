N, M = list(map(int, input().split()))
s = []

def dfs():
    print(s)
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

# N, M = list(map(int, input().split()))
# s = []
# visited = [False] * (N+1)
#
# def dfs():
#     if len(s) == M:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, N+1):
#         if (not visited[i]):
#             visited[i] = True
#             s.append(i)
#             dfs()
#             visited[i] = False
#             s.pop()
#
# dfs()
