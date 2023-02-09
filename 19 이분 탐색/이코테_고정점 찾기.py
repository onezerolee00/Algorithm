# 풀이 시간 20분 / 시간 제한 1초 / 메모리 제한 128MB / 기출 Amazon 인터뷰
# 소요 시간 8분

"""
만약 a[3]인데 그 값이 8이야 => 그말은 즉슨 더 왼쪽으로 가야 고정점이 존재한다
why? '오름차순'이기 때문이다
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

def binary_search(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        current = (left + right) // 2
        if array[current] == current:
            return current
        elif array[current] < current:
            left = current + 1
        else:
            right = current - 1

    return -1

print(binary_search(array))