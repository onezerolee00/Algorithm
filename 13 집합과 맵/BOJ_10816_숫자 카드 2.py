import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
N_cards = list(map(int, input().split()))
N_cards.sort()

M = int(input())
M_cards = list(map(int, input().split()))

N_Counter = Counter(N_cards)
for M_card in M_cards:
    if(M_card in N_Counter):
        print(N_Counter[M_card], end=' ')
    else:
        print(0, end=' ')
        
"""
방법 1) collecions 활용
방법 2) 이진탐색 활용
"""

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# N_cards = list(map(int, input().split()))
# N_cards.sort()
#
# M = int(input())
# M_cards = list(map(int, input().split()))
#
# for M_card in M_cards:
#     low = 0
#     high = len(N_cards) -1
#     cnt = 0
#     while(low<=high):
#         mid = (low+high) // 2;
#         if(N_cards[mid]==M_card):
#             cnt = N_cards[low:high+1].count(M_card)
#             break
#         elif(N_cards[mid] > M_card):
#             high = mid-1
#         else:
#             low = mid+1
#     print(cnt, end=' ')