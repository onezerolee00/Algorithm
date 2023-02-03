import sys
input = sys.stdin.readline
from itertools import combinations


n = int(input())

s = []
visited = [[False]*(n+1) for _ in range(n+1)]

for _ in range(n):
    s.append(list(map(int, input().split())))

i = [i for i in range(n)]

idx = list(combinations(i, n//2))

min = float('inf')

for id in idx: # 0, 1, 2
    start_stat = 0
    link_stat = 0
    id_ = []

    for i in range(n):
        if i not in list(id):
            id_.append(i)

    start_idx = list(combinations(list(id), 2))
    for start_idx in list(combinations(list(id), 2)):
        start_stat += s[start_idx[0]][start_idx[1]] + s[start_idx[1]][start_idx[0]]


    for link_idx in list(combinations(list(id_), 2)):
        link_stat += s[link_idx[0]][link_idx[1]] + s[link_idx[1]][link_idx[0]]

    if(min>abs(start_stat - link_stat)):
        min = abs(start_stat - link_stat)

print(min)