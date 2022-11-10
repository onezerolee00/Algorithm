import sys
input = sys.stdin.readline

str_list = []

for _ in range(int(input())):
    str = input().strip()
    if (str not in str_list):
        str_list.append(str)

str_list.sort(key = lambda x : (len(x), x))

for str in str_list:
    print(str)