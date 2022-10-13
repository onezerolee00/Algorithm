import sys

k = int(sys.stdin.readline())

for i in range(k):
    ps = sys.stdin.readline()
    ps_stack = list(ps)
    ps_stack.pop()

    right_brk_stack = []
    is_vps = True

    for j in range(len(ps_stack)):
        x = ps_stack.pop()
        if (x == ')'):
            right_brk_stack.append(x)
        elif (x == '(' and len(right_brk_stack) > 0):
            right_brk_stack.pop()
        elif (x == '(' and len(right_brk_stack) == 0):
            is_vps = False
            break

    if (len(right_brk_stack) > 0):
        is_vps = False

    if (is_vps):
        print('YES')
    else:
        print('NO')
