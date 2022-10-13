import sys

n = int(sys.stdin.readline())

case_num = 1
string_storage = []

for i in range(n):
    words = sys.stdin.readline().split()
    sentence = ''
    for j in range(len(words)):
        sentence += words.pop() + ' '
    string_storage.append(sentence)

for k in range(n):
    print("Case #"+ str(case_num)+":", string_storage[k])
    case_num += 1
