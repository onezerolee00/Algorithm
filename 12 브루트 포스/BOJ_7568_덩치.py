people = []
for _ in range(int(input())):
    people.append(list(map(int, input().split())))


for i in range(len(people)):
    rank = 1
    for j in range(len(people)):
        if(i!=j):
            if(people[i][0]<people[j][0] and people[i][1]<people[j][1]):
                rank += 1
    print(rank, end=" ")