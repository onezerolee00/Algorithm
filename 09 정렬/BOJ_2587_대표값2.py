n_list = []
for i in range(5):
    n_list.append(int(input()))
print(sum(n_list)//5)
n_list.sort()
print(n_list[2])