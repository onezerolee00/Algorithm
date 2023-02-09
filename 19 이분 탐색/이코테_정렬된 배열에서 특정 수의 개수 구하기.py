# 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128MB / 기출 Zoho 인터뷰
# 소요 시간 19분

import sys
input = sys.stdin.readline

"""
일단 target을 찾아
찾았어 그러면 또 다른 일을 해야함 => 바로 연속되는 왼쪽 끝점과 오른쪽 끝점을 찾는 것 (이걸 두개의 함수로 구현해보자!)
"""

def find_left_idx(array, target, idx):
    for i in range(idx, 0, -1):
        if array[i] == target:
            continue
        else:
            return i
    return i

def find_right_idx(array, target, idx):
    for i in range(idx, len(array)-1):
        if array[i] == target:
            continue
        else:
            return i
    return i

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        current = (left + right) // 2
        if array[current] == target:
            print(find_right_idx(array, target, current) - find_left_idx(array, target, current))
            break
        elif array[current] < target:
            left = current + 1
        else:
            right = current - 1

    print(-1)

n, x = map(int, input().split())
array = list(map(int, input().split()))


binary_search(array, x)