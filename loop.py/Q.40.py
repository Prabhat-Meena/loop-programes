d = "ABCDE"
a = 4
for i in range(1,10):
    if i<=5:
        for n in range(5-i):
            print(" ",end="")
        for j in range(i):
            print(d[j],end="")
    else:
        for m in range(i-5):
            print(" ",end="")
        for k in range(a):
            print(d[k],end='')
        a = a-1
    print()