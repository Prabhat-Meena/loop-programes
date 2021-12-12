al = "ABCDEF"
i = 1
e = 0
c = 0
while(i<=5):
    if i%2==0:
        b = 0
        while(b<i):
            print(al[c+b],end=" ")
            b = b+1
        c = c+2
    else:
        d = 1
        while(d<=i):
            print(d+e,end=" ")
            d = d+1
        if i<=2:
            e = e+1
        else:
            e = e+3
    i = i+1
    print()

