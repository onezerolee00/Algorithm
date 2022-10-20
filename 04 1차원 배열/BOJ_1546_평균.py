N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(N):
    scores[i] = scores[i]/M*100

print(sum(scores)/N)