cnt = 0
move_list = []

def hanoi(n, departures, arrivals, assistance): # (n: 옮길 원반 개수, departures: 출발 기둥, arrivals: 도착 기둥, assistant: 보조 기둥)
    global cnt
    if(n==1):
        cnt += 1
        move_list.append(str(departures) + ' ' + str(arrivals))
        return

    hanoi(n-1, departures, assistance, arrivals) # 원반 n-1개를 보조 기둥으로 옮긴다.
    cnt += 1
    move_list.append(str(departures) + ' ' + str(arrivals)) # 가장 큰 원반을 옮긴다.
    hanoi(n-1, assistance, arrivals, departures) # 보조기둥에 있는 원반 n-1개를 옮긴다.

hanoi(int(input()), 1, 3, 2)

print(cnt)
for move in move_list:
    print(move)

""""
1. 첫번째 기둥의 n-1개의 원반을 세번째 기둥으로 옮긴다.
2. 첫번째 기둥에 남은 원반 중 가장 큰 원반을 세번째 기둥으로 옮긴다.
3. 두번째 기둥에 있는 n-1개의 원반을 세번째 기둥으로 옮긴다.
"""