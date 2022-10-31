import sys
input = sys.stdin.readline

n_list = []
n_dict = {}

for i in range(int(input())):
    n = int(input())
    n_list.append(n)

    # 최빈값을 위한 코드. { key: 숫자, value: 빈도}
    if n not in n_dict:
        n_dict[n] = 1
    else:
        n_dict[n] += 1

# 산술평균
print(round(sum(n_list) / len(n_list)))

# 중앙값
n_sorted_list = sorted(n_list)
print(n_sorted_list[int((len(n_sorted_list)-1)/2)])


# 최빈값
n_sorted_dict = dict(sorted(n_dict.items(), key = lambda item: (item[1]), reverse=True)) # 빈도를 기준으로 내림차순 한다.
max_index = 0 # 가장 큰 빈도를 저장할 max_index

for index, (key, value) in enumerate(n_sorted_dict.items()): # 내림차순되었기 때문에 가장 첫번째 요소의 value만 가져온다.
    max_index = value
    break

key_list = [] # max_index(가장 큰 빈도)를 가진 key(숫자)들을 저장할 리스트
for index, (key, value) in enumerate(n_sorted_dict.items()): # value(빈도)가 max_index(가장 큰 빈도)와 같다면 append
    if(value == max_index):
        key_list.append(key)
    else:
        break

key_list.sort() # 두번째로 작은 key를 출력
if(len(key_list) > 1):
    print(key_list[1])
else:
    print(key_list[0])

# 범위
print(max(n_list) - min(n_list))


"""
활용하면 좋을 라이브러리 : Counter
"""