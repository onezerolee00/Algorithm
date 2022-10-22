def check_group_word(word):
    index = 0
    char_list = []
    while (index < len(word)):
        if (word[index] in char_list):
            return False
        ck_index = 1
        if (index + ck_index == len(word)):
            break
        while (word[index] == word[index + ck_index]):
            ck_index += 1
            if(index+ ck_index == len(word)):
                break
        char_list.append(word[index])
        index += ck_index
    return True

N = int(input())
group_word_num = 0

for i in range(N):
    word = input()
    if(check_group_word(word)):
        group_word_num += 1

print(group_word_num)