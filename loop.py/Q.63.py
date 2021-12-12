a = 3
for i in range(1,10):
    if i<=4:
        for j in range(i):
            print("*",end="")
    else:
        for k in range(a):
            print("*",end='')
        a = a-1
    print()