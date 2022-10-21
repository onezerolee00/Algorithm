S = list(input())

for i in range(97, 123):
    if(chr(i) not in S):
        print(-1, end=' ')
    else:
        print(S.index(chr(i)), end=' ')

# 97~122