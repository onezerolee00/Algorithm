# k개의 랜선 => n개의 같은 길이의 랜선
# n개를 만들 수 있는 랜선의 최대 길이

"""
0~max(array)의 중간값으로 이진탐색
랜선의 개수가 많이 나오면 더 크게 잘라야 하니 cut 기준 높이기

1트 틀린이유 : [N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다.] 고려안함
2트 틀린이유 : left의 초기값을 1이 아닌 0으로 설정
3트 틀린이유 : [[최대 길이]] 를 구해야한다는 것을 간과
"""

import sys
input = sys.stdin.readline

def binary_search(array, target):
    left = 1
    right = max(array)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for lan in array:
            cnt += lan // mid
            print(cnt, mid)

        # if cnt == target: 이 부분이 패인
        #     return mid
        if cnt < target:
            right = mid - 1
        else:
            left = mid + 1
    return right

# 입력
k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

print(binary_search(array, n))