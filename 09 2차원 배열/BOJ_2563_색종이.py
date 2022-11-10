paper = [[0]*101 for i in range(101)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

cnt = 0
for row in paper:
    for p in row:
        if(p == 1):
            cnt += 1

print(cnt)


"""
색종이의 위치에 맞게 도화지 배열(101*101)에 1을 대입.
"""