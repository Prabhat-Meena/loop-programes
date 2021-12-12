d = 9
for i in range(1,4):
    for j in range(1):
        print(d,end="")
        d=d-1
    if i>1:
        c = d-1
        for k in range(1):
            print(" ",c,end=" ")
    if i>2:
        y = c-2
        for t in range(1):
            print(y,end="")
    print()
i = 4
g = 4
for l in range(1,3):
    j = 0
    for o in range(g):
        print(i-j,end=" ")
        j=j+2
    i=i-3
    print()
    g=g+1