C = int(input())

for i in range(C):
    scores = list(map(int, input().split()))
    scores.reverse()
    N = scores.pop()
    average = sum(scores)/N
    std_over_avg = 0
    for student in scores:
        if(student>average):
            std_over_avg += 1
    print('%.3f' %(std_over_avg/N*100), end="%\n")