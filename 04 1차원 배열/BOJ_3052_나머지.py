remainder = []
for i in range(10):
    x = int(input())%42
    if(x not in remainder):
        remainder.append(x)
print(len(remainder))