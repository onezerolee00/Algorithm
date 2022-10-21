sentence = input()
blk_minus = 0

if(sentence[0]==' '):
    blk_minus += 1
if(sentence[-1]==' '):
    blk_minus += 1

print(sentence.count(' ')-blk_minus+1)

'''
문자열이 공백으로 시작하거나 끝날 수 있으므로 이를 blk_minus를 이용해 고려해주었다.
'''