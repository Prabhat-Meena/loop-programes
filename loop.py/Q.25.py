a = 4
for i in range(1,10):
    if i<=5:
        for j in range(i):
            print(i,end="")
    else:
        for k in range(a):
            print(a,end='')
        a = a-1
    print()

