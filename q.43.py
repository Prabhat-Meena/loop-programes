a = 1
c = 0
g = 0
while(a<=5):
    if a>1 and a<5:
        b = 1
        while(b<=a):
            print(c, end=" ")
            c=c+1
            b=b+1
    else:
        k = 9
        if a<2 or a>4:
            print(k,end=" ")
    if a>4:
        d = 2
        while(d<=a):
            print(g,end=" ")
            d = d+1
            g = g+1
    print()
    a=a+1