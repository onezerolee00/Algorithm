A, B = map(str, input().split())

A = list(A)
A.reverse()
A = A[0] + A[1] + A[2]

B = list(B)
B.reverse()
B = B[0] + B[1] + B[2]

print(A if A>B else B)