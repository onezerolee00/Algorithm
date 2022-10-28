import sys
input = sys.stdin.readline

n_list = [0] * 10001
for i in range(int(input())):
    n = int(input())
    n_list[n] += 1

for i in range(1, len(n_list)):
    if(n_list[i] != 0):
        for j in range(n_list[i]):
            print(i)

"""
계수 정렬 (Counting Sort)
1. 데이터가 모두 담길 수 있는 리스트를 생성한다.
2. 모든 데이터를 확인하며 값과 동일한 인덱스의 데이터를 1씩 증가
"""

"""
메모리 초과 :
n_list에 수를 입력받고 그 수에 맞게 index_list를 또 생성하여 계수 정렬을 활용했다.
리스트를 두 개 써서 메모리 초과를 야기했다.
따라서, 리스트를 하나 쓰도록 코드를 수정해주었다.
"""