# # array에 target_array의 원소들이 있는 지 구하는 문제
# import sys
# input = sys.stdin.readline
#
# # 재귀를 이용한 이분탐색 (존재하면 1, 존재하지 않으면 0을 return한다.)
# def binary_search(array, target, left, right):
#     if left > right: # 존재하지 않음
#         return 0
#     current = (left+right) // 2
#     print(left, right, current, array[current], target)
#
#     if array[current] == target:
#         print('dfdf')
#         return 1
#     elif array[current] < target:
#         binary_search(array, target, current+1, right)
#     else:
#         binary_search(array, target, left, current-1)
#
# # 입력 받기
# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
# # 1 2 3 4 5
#
# m = int(input())
# target_array = list(map(int, input().split()))
#
# for target in target_array:
#     print(binary_search(array, target, 0, n-1))

# array에 target_array의 원소들이 있는 지 구하는 문제
import sys
input = sys.stdin.readline

# 반복문을 이용한 이분탐색 (존재하면 1, 존재하지 않으면 0을 return한다.)
def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        current = (left+right) // 2
        if array[current] == target:
            return 1
        elif array[current] < target:
            left = current + 1
        else:
            right = current - 1
    return 0

# 입력 받기
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
target_array = list(map(int, input().split()))

# 탐색 함수 호출
for target in target_array:
    print(binary_search(array, target))