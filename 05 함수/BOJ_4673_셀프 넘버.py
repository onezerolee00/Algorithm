def d(n):
    n_list = list(map(int, str(n)))
    return n + sum(n_list)

not_self_number = []

for i in range(1, 10001):
    if(d(i) not in not_self_number):
        not_self_number.append(d(i))

for i in range(1, 10001):
    if(i not in not_self_number):
        print(i)

'''
셀프 넘버가 아닌 수를 d 함수를 이용하여 not_self_number에 넣고
not_self_number에 없는 수(셀프 넘버)를 출력
'''