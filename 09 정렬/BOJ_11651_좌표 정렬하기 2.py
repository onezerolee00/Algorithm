import sys
input = sys.stdin.readline

coord_list = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    coord_list.append([x, y])

coord_list.sort(key = lambda x: (x[1], x[0]))

for coord in coord_list:
    print(coord[0], coord[1])