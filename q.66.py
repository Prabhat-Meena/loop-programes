g = "ABC"
a = 3
while(a>=1):
    i = 0
    while(i<a):
        print(g[i],end='')
        i = i + 1
    
    if a>1:
        if a ==2:
            print(" ",end="")
        b = 1
        while(b>=0):
            print(g[b],end='')
            b = b-1
    else:
        h = 1
        while(h<=1):
            print("  ","A",end="")
            h = h+1
    print()
    a=a-1


i = "ABC"
a = 1
t = 1
while(a<=2):
    b = 0
    d = 1
    while(b<=a):
        print(i[b],end="")
        d = d+1
        b = b+1
    while(t<=1):
        print(" ",end="")
        t = t+1
    b = 1
    while(b>=0):
        print(i[b],end="")
        b = b-1
    a = a+1
    print()