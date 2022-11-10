def star(n, stars):
    global N
    N *= 3
    star_list = []

    for i in range(3):
        for j in range(N//3):
            if (i!=1): # 공백이 없는 1, 3번째 그룹
                star_list.append(stars[j] * 3)
            if (i==1): # 공백이 있는 2번째 그룹
                star_list.append(stars[j] + ' '*(N//3) + stars[j])

    if(N!=n): # N이 아직 n(N_input)에 도달하지 못했으면 재귀함수 호출
        star(n, star_list)
    else: # N이 n(N_input)에 도달하면 최종 문자열이 완성되었다는 뜻. 출력.
        for s in star_list:
            print(s)

N = 1
N_input = int(input())
star(N_input, ['*'])

"""
인자로 들어온 stars(이전의 star_list)를 이용해 현재 N에 해당하는 각 문자열을 한 줄 씩 생성해 star_list에 append 한다.
e.g.) N이 3일 경우 star_list = ['***', '* *', '***']가 된다. 
"""