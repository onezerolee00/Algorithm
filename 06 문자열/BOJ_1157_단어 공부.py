string = input()

alphabet = [0 for i in range(26)]

for char in string:
    ck_num = ord(char.lower())
    alphabet[ck_num-97] += 1

max_index = alphabet.index(max(alphabet))
max_num = max(alphabet)
del alphabet[max_index]
if(max_num == max(alphabet)):
    print('?')
else:
    print(chr(max_index+65))


'''
가장 많이 쓰인 알파벳의 인덱스와 횟수를 저장하고 해당 요소를 삭제시켜서
나머지 요소 중에서도 같은 횟수가 있는 지 점검을 함으로써 가장 많이 사용된 알파벳이 여러 개 존재하는 경우를 점검한다.
'''

# 97~122
# 65~90