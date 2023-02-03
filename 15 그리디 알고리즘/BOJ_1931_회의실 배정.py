n = int(input())
meetings = []

for i in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key=lambda x:(x[1], x[0]))
# end 오름차순 후 start 오름차순

answer = 1
prev_end = meetings[0][1]

for i in range(1, n):
    if prev_end <= meetings[i][0]:
        answer += 1
        prev_end = meetings[i][1]

print(answer)
