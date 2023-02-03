import sys
input = sys.stdin.readline

def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        current = (left + right) // 2
        if array[current] == target:
            return True
        elif array[current] < target:
            left = current + 1
        else:
            right = current - 1

    return False

N = int(input().rstrip())
array = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
target_list = list(map(int, input().rstrip().split()))

array.sort()

for target in target_list:
    if binary_search(array, target):
        print('yes', end=" ")
    else:
        print('no', end=" ")