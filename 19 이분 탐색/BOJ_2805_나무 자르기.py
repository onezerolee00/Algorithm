"""
자르고 남은 나무의 길이가 target보다 크면 더 크게 잘라야함
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

# target : 상근이가 집으로 가져가려고 하는 나무의 길이 M
def binary_search(array, target):
    left, right = 1, max(array)

    while left <= right:
        mid = (left+right) // 2
        tree_sum = 0

        for tree in array:
            if tree >= mid:
                tree_sum += tree - mid

        if tree_sum >= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(binary_search(array, m))