import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9


def dfs(d, total, plus, minus, mul, div):
    # 연산을 모두 끝낼 때마다 max와 min을 갱신해준다.
    global maximum, minimum
    if d == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # dfs를 호출 시마다 연산 길이는 증가하고, 연산자의 수는 감소하도록 호출
    if plus:
        dfs(d+1, total+num[d], plus-1, minus, mul, div)
    if minus:
        dfs(d+1, total-num[d], plus, minus-1, mul, div)
    if mul:
        dfs(d+1, total*num[d], plus, minus, mul-1, div)
    if div:
        dfs(d+1, int(total/num[d]), plus, minus, mul, div-1)


dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])
print(maximum)
print(minimum)

# N = int(input())
# A = list(map(int, input().split()))
# operator_num = list(map(int, input().split()))
#
# def get_operator(operator_num):
#     operator = []
#     for i in range(len(operator_num)):
#         if(i==0):
#             for j in range(operator_num[i]):
#                 operator.append('+')
#         elif(i==1):
#             for j in range(operator_num[i]):
#                 operator.append('-')
#         elif(i==2):
#             for j in range(operator_num[i]):
#                 operator.append('*')
#         elif(i==3):
#             for j in range(operator_num[i]):
#                 operator.append('//')
#     return operator
#
# operator = get_operator(operator_num)
#
# result = []
# s = []
# visited = [False] * (sum(operator_num) + 1)
# prev = 0
# def dfs():
#     global prev
#     if len(s) == sum(operator_num):
#         for i in range(len(s)):
#             if (i == 0):
#                 prev = eval(str(A[0]) + s[0] + str(A[1]))
#                 print(str(A[0]) + s[0] + str(A[1]))
#             else:
#                 x = prev
#                 prev = eval(str(x) + s[i] + str(A[i+1]))
#                 print(str(x) + s[i] + str(A[i+1]))
#         print(prev)
#         result.append(prev)
#         prev = 0
#         return
#
#     for i in range(1, sum(operator_num) + 1):
#         if not visited[i]:
#             visited[i] = True
#             s.append(operator[i-1])
#             dfs()
#             visited[i] = False
#             s.pop()
#
# dfs()
#
# print(max(result))
# print(min(result))
"""
이전 코드: 시간초과 파티,,
"""

