"""
[입력]
N(3 <= N <= 100) : 카드의 개수
M(10 <= M <= 300,000) : 딜러가 외친 숫자.

[출력]
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력해야 한다.

"""

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
max_sum = 0
sum_card = 0
a, b, c = 0, 0, 0

for i in range(len(card_list)-2):
    for j in range(i+1, len(card_list)-1):
        for k in range(j+1, len(card_list)):
            a = card_list[i]
            b = card_list[j]
            c = card_list[k]
            sum_card = a + b + c
            if(a+b+c > M):
                continue
            else:
                if(max_sum < sum_card):
                    max_sum = sum_card

print(max_sum)