import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

graph = []
loc_of_0 = []

for i in range(n):
    row = list(map(int, input().split(' ')))
    graph.append(row)
    for j in range(m):
        if row[j] == 0:
            loc_of_0.append((j, i))

com = list(combinations(loc_of_0, 3))
print(len(com))