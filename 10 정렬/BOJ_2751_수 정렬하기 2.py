import sys
input = sys.stdin.readline
n_list = []
for i in range(int(input())):
    n_list.append(int(input()))

n_list.sort()
for n in n_list:
    print(n)

"""
시간초과가 발생하지 않도록 sys.stdin.readline을 사용하도록 하자
"""