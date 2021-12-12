a = 6
i = 0
while(a>=1):
    o = 1
    while(o<=a):
        print(o,end="")
        o = o+1
    b = 1
    while(b>a):
        print(b,end="")
        b = b-1
    j = 1
    d = 6
    while(j<=a):
        print(d-i,end="")
        j = j+1
        d = d-1
    a = a-1
    print()
    i = i+1