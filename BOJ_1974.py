import sys

n = int(sys.stdin.readline())

stack = list(range(n, 0, -1))


sequence_std = []
tmp = []
string_pm = []
avail = True

for i in range(n):
    sequence_std.append(int(sys.stdin.readline()))

sequence_std.reverse()


while(sequence_std):
    if(len(stack)==0):
        break
    x = stack.pop()
    tmp.append(x)
    string_pm.append('+')

    if(sequence_std[-1]==x):
        tmp.pop()
        sequence_std.pop()
        string_pm.append('-')

        while(True):
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
    elif(sequence_std[-1]<x):
        avail=False

string_pm.reverse()

if(not avail):
    print("NO")
else:
    while(string_pm):
        print(string_pm.pop())

# 비교하려는 -1 얘가 작아? 그건 있을 수 없는 일