"""
내가 찾고 싶은거는 값의 최소
그러면 -붙은 애가 가장 커지게 괄호 해줘야함
"""

string = input()
plus = string.split('-')

for i in range(1, len(plus)):
    digits = plus[i].split('+')
    digits = list(map(int, digits))
    plus[i] = sum(digits)

print(sum(list(map(int, plus[0].split('+')))) - sum(plus[1:]))
# print(int(plus[0]) - sum(plus[1:]))