N = int(input())
result = 0

for i in range(1, 1000001):
    i_sum = i
    i_list = list(map(int, str(i)))
    i_sum += sum(i_list)
    if(i_sum == N):
        result = i
        break

print(result)

"""
런타임 에러 : while 문을 사용
"""
