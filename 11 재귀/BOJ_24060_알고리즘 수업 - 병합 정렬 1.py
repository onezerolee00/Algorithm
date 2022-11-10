# 문제에 적힌 것 대로 + cnt만 추가해서 작성을 했으나 아직 이해 못 함.... 다시 봐야함

import sys
input = sys.stdin.readline

A, K = map(int, input().split())
array = list(map(int, input().split()))

def merge_sort(A, p, r):
    if (p < r and cnt <= K):
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, result
    i = p
    j = q+1
    t = 1
    tmp = []
    while(i<=q and j <=r):
        if (A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while(i<=q):
        tmp.append(A[i])
        i += 1
    while(j<=r):
        tmp.append(A[j])
        j += 1

    i = p
    t = 0

    while(i<=r):
        A[i] = tmp[t]
        cnt += 1
        if(cnt==K):
            result = A[i]
            break
        i += 1
        t += 1

cnt = 0
result = -1
merge_sort(array, 0, A-1)
print(result)