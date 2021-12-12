i = 1
a = 2
d = 1
while(i<=7):
    if i%2==0:
        b = 1
        s = 0
        while(b<=2):
            print(a+s,end="")
            s = s+1
            b = b+1
        a = a+3
    else:
        print(d,end="")
        d = d+3
    print()
    i = i+1