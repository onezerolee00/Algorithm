import sys

count = 1
sticks = []
ea = int(sys.stdin.readline())

for i in range(ea):
    sticks.append(int(sys.stdin.readline()))

max = sticks.pop()

while(sticks):
    x = sticks.pop()
    if(x > max):
        max = x
        count += 1

print(count)
