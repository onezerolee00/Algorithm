student = [i for i in range(1, 31)]

for i in range(28):
    student.remove(int(input()))

print(min(student))
print(max(student))


"""
원래는 인덱스를 이용하여 출석번호를 입력 받을 때 1을 더한 뒤에 0인 요소만 출력했는데
계속 틀렸습니다가 나와 remove를 이용한 풀이로 변경. 
"""