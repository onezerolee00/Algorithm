max_int = 0
N, M = 0, 0

for i in range(9):
    A = list(map(int, input().split()))
    a = max(A)
    if (a > max_int):
        N = i
        M = A.index(a)
        max_int = a

print(max_int)
print(N + 1, M + 1)