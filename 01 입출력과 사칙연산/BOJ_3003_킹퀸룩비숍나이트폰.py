pieces = list(input().split())
pieces_std = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(pieces_std[i]-int(pieces[i]), end=" ")