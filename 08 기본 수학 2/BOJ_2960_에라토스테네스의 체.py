N, K = map(int, input().split())

num_list = [i for i in range(2, N+1)]

cnt = 0

while(num_list):
    min_num = min(num_list)
    for n in num_list:
       if(n%min_num == 0):
           num_list.remove(n)
           cnt += 1
           if(cnt==K):
               print(n)