i = 5
k = 3
j = 1
r = 0
t = 3
while(i>=1):
    if i<5:
        f = 1
        g = 3
        while(f<=j):
            print(g,end="")
            g = g-1
            f = f+1
        j = j+1
    b = 1
    while(b<=i):
        print(k,end="")
        b = b+1
    if i<5:
        h = 0
        while(h<=r):
            print(t+h,end="")
            h = h+1
        t = t-1
        r = r+1
    i = i-2
    k = k-1
    print()


i = 3
a = 2
x = 1
y = 3
while(i>=1):
    g = 1
    while(g<=x):
        print(y,end="")
        g = g+1
    b = 1
    while(b<=i):
        print(a,end="")
        b = b+1
    h = 1
    while(h<=x):
        print(y,end="")
        h = h+1
    a = a+1
    i = i-2
    x = x+1
    print()