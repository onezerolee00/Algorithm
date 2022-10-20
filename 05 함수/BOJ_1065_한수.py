N = int(input())
count = 0
for i in range(1, N+1):
    if(i<=99):
        count += 1
    else:
        n_list = list(map(int, str(i)))
        if(n_list[0] - n_list[1] == n_list[1] - n_list[2]):
            count += 1
print(count)
