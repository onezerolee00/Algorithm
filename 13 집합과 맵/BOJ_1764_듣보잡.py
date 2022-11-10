import sys
input = sys.stdin.readline

N, M = map(int, input().split())

first_dict = {}
for i in range(N):
    first_dict[input().rstrip()] = 0

second_dict = {}
for j in range(M):
    second_dict[input().rstrip()] = 0

third_dict = {}
if(N>=M):
    for key, value in first_dict.items():
        if(key in second_dict):
            third_dict[key] = 0
else:
    for key, value in second_dict.items():
        if(key in first_dict):
            third_dict[key] = 0

sorted_third_list = sorted(third_dict.items())
sorted_third_dict = dict(sorted_third_list)

print(len(sorted_third_dict))
for key, value in sorted_third_dict.items():
    print(key)