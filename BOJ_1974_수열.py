import sys

n = int(sys.stdin.readline()) # 수열의 길이를 입력 받는다.

stack = list(range(n, 0, -1))

sequence_std = [] # 만들고자 하는 수열
tmp = [] # 수열을 만들기 위해 잠깐 숫자를 담아 둘 스택
string_pm = [] # 출력할 '+', '-' 문자들
avail = True # 수열을 만들 수 있는 지에 대한 여부

for i in range(n): # 수열을 입력 받는다.
    sequence_std.append(int(sys.stdin.readline()))

sequence_std.reverse() # 1, 2, 3, .. 순서로 pop하면서 체크할 것이므로 역순으로 저장


while(sequence_std):
    if(len(stack)==0):
        break

    # 우선 처음에는 무조건 push
    x = stack.pop()
    tmp.append(x)
    string_pm.append('+')

    # push된 숫자 점검 후 비교
    if(sequence_std[-1]==x): # 만약 같으면 pop
        tmp.pop()
        sequence_std.pop()
        string_pm.append('-')

        while(True): # 한 번 pop 하면 그 아래 stack도 점검해줘야 한다.
            if(len(tmp)==0):
                break
            t = tmp.pop()
            if(sequence_std[-1]==t):
                sequence_std.pop()
                string_pm.append('-')
            elif(sequence_std[-1]<x):
                avail=False
            else:
                tmp.append(t)
                break

    elif(sequence_std[-1]<x): # 기준이 stack의 top 보다 작으면 수열을 만들 수 없다.
        avail=False

string_pm.reverse()

if(not avail):
    print("NO")
else:
    while(string_pm):
        print(string_pm.pop())
