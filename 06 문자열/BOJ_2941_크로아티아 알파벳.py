alphabet_num = 0
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
input_string = input()
index = 0

while(index < len(input_string)):
    if(input_string[index:index+2] in croatia):
        alphabet_num += 1
        index += 2
    elif(input_string[index:index+3] in croatia):
        alphabet_num += 1
        index += 3
    else:
        alphabet_num += 1
        index += 1

print(alphabet_num)

"""
변경되어 입력되는 크로아티아 알파벳에서 가장 길이가 긴 것이 3이기 때문에
index를 기준으로 2개의 길이 알파벳, 3개의 길이 알파벳을 나눠서 검사한다.
"""