import sys

k = int(sys.stdin.readline())

stack = []

for i in range(k):
    input_integer = int(sys.stdin.readline())
    stack.append(input_integer)
    if(input_integer == 0):
        stack.pop()
        stack.pop()

print(sum(stack))