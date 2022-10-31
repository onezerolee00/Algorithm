import sys
input = sys.stdin.readline

member_list = []

for i in range(int(input())):
    age, name = map(str, input().split())
    member_list.append([int(age), name, i])

member_list.sort(key = lambda x: (x[0], x[2]))

for member in member_list:
    print(member[0], member[1])