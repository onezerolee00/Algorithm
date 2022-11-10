# 보드 -> 체스판

# 보드의 크기 입력 받기
N, M = map(int, input().split())

# 보드의 색깔 입력 받기
board = []
for _ in range(N):
    board.append(input())

# 체스판을 색칠하는 경우 1) 맨 왼쪽 위 칸이 'W'인 경우
chess_board_1 = []
for i in range(8):
    buffer = ''
    for j in range(8):
        if(i%2==0):
            if(j%2==0):
                buffer += 'W'
            else:
                buffer += 'B'
        else:
            if(j%2==0):
                buffer += 'B'
            else:
                buffer += 'W'
    chess_board_1.append(buffer)

# 체스판을 색칠하는 경우 2) 맨 왼쪽 위 칸이 'B'인 경우
chess_board_2 = []
for i in range(8):
    buffer = ''
    for j in range(8):
        if(i%2==0):
            if(j%2==0):
                buffer += 'B'
            else:
                buffer += 'W'
        else:
            if(j%2==0):
                buffer += 'W'
            else:
                buffer += 'B'
    chess_board_2.append(buffer)

# 다시 칠하는 횟수를 저장한다.
repaint = []

# i, j는 체스 시작점
for i in range(N-7):
    for j in range(M-7):
        # 체스판과 보드를 비교하며 다시 칠하는 경우를 센다.
        cnt1 = 0
        cnt2 = 0
        # 체스판과 보드를 하나하나 비교한다.
        for k in range(8):
            for l in range(8):
                # 체스판과 보드를 비교하며 다르면 다시 색칠한다.
                if(board[i+k][j+l] != chess_board_1[k][l]):
                    cnt1 += 1
                if(board[i+k][j+l] != chess_board_2[k][l]):
                    cnt2 += 1
        repaint.append(cnt1)
        repaint.append(cnt2)

# 다시 색칠하는 횟수 중 가장 작은 값을 출력
print(min(repaint))
