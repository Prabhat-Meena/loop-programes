i = 1
d = 1
g = 1
k = 1
while(i<=3):
    if d == 5:
        b = 1
        while(b<=d+1):
            print(g,end=' ')
            b = b+1
            g = g+2
    else:
        b = 1
        while(b<=d):
            print(g,end=" ")
            b = b+1
            g = g+2
    i = i+1
    d  = d+2
    print()