a = 3
while(a>=1):
    i = 1
    while(i<=a):
        print(i,end='')
        i = i+1
    
    if a>1:
        if a ==2:
            print(" ",end="")
        b = 2
        while(b>=1):
            print(b,end='')
            b = b-1
    else:
        h = 1
        #while(h<=1):
        print("  ",h,end="")
        #    h = h+1
    print()
    a = a-1

a = 1
t = 1
while(a<=2):
    b = 0
    d = 1
    while(b<=a):
        print(d,end="")
        d = d+1
        b = b+1
    while(t<=1):
        print(" ",end="")
        t = t+1
    b = 1
    while(b<=2):
        print(b,end="")
        b = b+1
    a = a+1
    print()