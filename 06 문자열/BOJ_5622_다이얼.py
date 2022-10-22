word = input()
dial_alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
min_time = 0

for char in word:
    for i in range(len(dial_alphabet)):
        if(char in dial_alphabet[i]):
            min_time += dial_alphabet.index(dial_alphabet[i]) + 3

print(min_time)