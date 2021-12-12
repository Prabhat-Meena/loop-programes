i = 1
g = 5
d = 9
while(i<=3):
    b = 1
    while(b<=1):
        print(d,end="")
        b = b+1
        d = d-1
    if i>1:
        c = d-1
        n = 1
        while(n<=1):
            print("",c,end=" ")
            n = n+1
    g = g+1
    if i>2:
        y = c-2
        j = 1
        while(j<=1):
            print(y,end=" ")
            j = j+1
    print()
    i = i+1

i = 4
g = 4
a = 1
while(a<=2):
    b = 1
    j = 0
    while(b<=g):
        print(i-j,end=" ")
        b = b+1
        j = j+2
    a = a+1
    i = i-3
    print()
    g = g+1