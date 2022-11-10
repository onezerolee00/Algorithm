N = int(input())
sanggeun_cards = list(map(int, input().split()))

M = int(input())
comparison_cards = list(map(int, input().split()))

sanggeun_dict = {}

for i in range(len(sanggeun_cards)):
    sanggeun_dict[sanggeun_cards[i]] = 0

for c_card in comparison_cards:
    if(c_card in sanggeun_dict):
        print(1, end=" ")
    else:
        print(0, end=" ")


"""
풀이 1) 속도가 빠른 dictionary 자료구조를 사용하는 방법
풀이 2) 이진 탐색
"""