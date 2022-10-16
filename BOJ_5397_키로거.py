import sys

n = int(sys.stdin.readline()) # 테스트 케이스 개수 입력 받기

for i in range(n): # 테스트 케이스의 수 만큼 반복
    keylogger = list(sys.stdin.readline()) # 키로거 입력 받기
    keylogger.pop() # \n는 삭제
    keylogger.reverse()
    left = [] # 커서 기준 왼쪽 스택
    right = [] # 커서 기준 오른쪽 스택

    while (keylogger): # 키로거가 빌 때까지 반복한다.
        x = keylogger.pop() # pop 하면서 점검
        if (x == '<'): # 커서를 왼쪽으로 이동 (왼쪽 스택 top에 있는 것을 오른쪽 스택에 push)
            if (len(left) != 0):
                y = left.pop()
                right.append(y)
        elif (x == '>'): # 커서를 오른쪽으로 이동 (오른쪽 스택 top에 있는 것을 왼쪽 스택에 push)
            if (len(right) != 0):
                y = right.pop()
                left.append(y)
        elif (x == '-'): # 왼쪽 스택 top에 있는 것을 pop 해서 백스페이스 구현
            if (len(left) != 0):
                left.pop()
        else: # 나머지 문자는 왼쪽 스택에 push
            left.append(x)
    right.reverse()
    password = ''.join(left) + ''.join(right)
    print(password)

'''
커서 기준으로 왼쪽 스택과 오른쪽 스택을 나눈다. 
keylogger에서 하나씩 pop() 하면서 문자에 맞게 처리해준다.
주의할 점은 오른쪽 스택은 reverse를 해줘야한다는 점이다.

처음에는 인덱스로 커서 역할을 구현하려고 했다. 
'''