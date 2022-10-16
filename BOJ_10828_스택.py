import sys

def push(stack, x):
    stack.append(x)

def pop(stack):
    if(len(stack)==0):
        print(-1)
        return
    print(stack.pop())

def size(stack):
    print(len(stack))

def empty(stack):
    if(len(stack)==0):
        print(1)
    else:
        print(0)

def top(stack):
    if(len(stack)==0):
        print(-1)
        return
    print(stack[-1])

def func(command):
    if(len(command) == 2):
        eval(str(command[0])+'(stack, '+str(command[1])+')')
    else:
        eval(str(command[0])+'(stack)')


stack = []
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    func(command)

