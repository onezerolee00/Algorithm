int_list = []
for i in range(9):
    int_list.append(int(input()))

print(max(int_list))
print(int_list.index(max(int_list))+1, end='')