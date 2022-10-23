import math
A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))

"""
A*x - B*(x-1) > V 가 성립하는 가장 작은 자연수 x를 구하면 된다.
"""