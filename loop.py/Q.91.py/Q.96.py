a ="ABC"
c = 0
for i in range(1,4):
    for j in range(i):
        print(a[c],end="")
    print()
    for k in range(i):
        print(i,end="")
    c=c+1
    print()
