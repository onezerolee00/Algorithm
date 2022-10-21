T = int(input())

for i in range(T):
    R, S = input().split()
    S = list(S)
    for s in S:
        print(int(R) * s, end='')
    print()

'''
처음에 틀렸던 이유 : print()로 줄바꿈을 해주지 않아서 틀렸다.
'''