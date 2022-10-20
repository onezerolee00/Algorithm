N, X = map(int, input().split())
sequence = list(input().split())

for number in sequence:
    if(int(number)<X):
        print(number, end=" ")