N = int(input())

for i in range(N):
    quiz = input()
    score = 0
    accumulate = 0

    for answer in quiz:
        if(answer=='O'):
            accumulate += 1
            score += accumulate
        else:
            accumulate = 0
    print(score)