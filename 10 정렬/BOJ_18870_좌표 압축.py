import sys
input = sys.stdin.readline

#  { key: 좌표, value: 압축된 좌표 }
coord_dict = {}

# 입력
N = int(input())
coord_list = list(map(int, input().split()))

# 중복 없이 정렬된 좌표 리스트로 딕셔너리 정보를 생성한다.
sorted_coord_list = sorted(list(set(coord_list)))

# 제일 작은 좌표 순으로 0, 1, 2, ... 를 압축된 좌표로 사용한다.
for i in range(len(sorted_coord_list)):
    coord_dict[sorted_coord_list[i]] = i
    # 없어도 되는 코드.
    #if(i!=0 and sorted_coord_list[i-1] == sorted_coord_list[i]):
    #    coord_dict[sorted_coord_list[i]] -= 1

for coord in coord_list:
    print(coord_dict[coord], end=' ')