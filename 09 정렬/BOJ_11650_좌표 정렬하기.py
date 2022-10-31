import sys
input = sys.stdin.readline

coord_list = []
for i in range(int(input())):
    x, y = map(int, input().split())
    coord_list.append([x, y])

coord_list = sorted(coord_list)
for coord in coord_list:
    print(coord[0], coord[1])

"""
sort(key=lambda x: (x[1]))도 알아두면 좋을 것 같다.
"""