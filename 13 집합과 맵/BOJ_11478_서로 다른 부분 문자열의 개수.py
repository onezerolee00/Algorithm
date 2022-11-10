S = list(input())
subset_dict = {}

for i in range(1, len(S)+1):
    for j in range(len(S)-i+1):
        x = ''.join(S[j:j+i])
        subset_dict[x] = 0

print(len(subset_dict))
