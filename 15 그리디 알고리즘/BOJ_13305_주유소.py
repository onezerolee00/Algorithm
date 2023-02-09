"""
나보다 작은 애 검색해서 그 도로까지만 산다
"""

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# distances = list(map(int, input().split()))
# stations = list(map(int, input().split()))
# price = 0
# distance = 0
#
# for i in range(len(stations)):
#     cnt = 0
#     if distance == sum(distances):
#         price += stations[i] * cnt
#         break
#     for j in range(i, len(stations)):
#         if stations[i] <= stations[j]:
#             if j == len(stations)-1:
#                 break
#             cnt += distances[j]
#             distance += distances[j]
#     price += stations[i] * cnt
#
# print(price)

import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
stations = list(map(int, input().split()))
price = stations[0] * distances[0]
min_price = stations[0]
distance = 0

for i in range(1, len(stations)-1):
    if stations[i] < min_price:
        price += min_price * distance
        distance = distances[i]
        min_price = stations[i]
    else:
        distance += distances[i]

    if i == n-2:
        price += min_price*distance

print(price)
