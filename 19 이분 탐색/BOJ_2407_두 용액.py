"""
같은 양의 두 용액을 혼합한 용액의 특성 값 = 혼합에 사용된 각 용액의 특성값의 합
특성값 0에 가까운 용액 만들려고 함


"""
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

answer = [0, 0]

left, right = 0, len(array)-1
prev = float('inf')

while left < right:
    value = array[left] + array[right]
    if abs(value) < prev:
        prev = abs(value)
        answer = [array[left], array[right]]

    if value < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
