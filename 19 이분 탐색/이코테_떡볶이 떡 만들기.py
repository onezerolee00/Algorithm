import sys
input = sys.stdin.readline

# N(떡의 개수), M(요청한 떡의 길이) 입력
n, request = map(int, input().split())

# array(떡의 개별 높이) 입력
array = list(map(int, input().split()))


def get_cut(array, request):
    left = 0
    right = max(array)

    while left <= right:
        rest = 0
        cut = (left + right) // 2
        for rice in array:
            if rice >= cut:
                rest += rice - cut
        if rest == request:
            return cut
        elif rest > request:
            left = cut + 1
        else:
            right = cut - 1

print(get_cut(array, request))