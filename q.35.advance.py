i = 0
a = 1
p = 4
k = 7
s = 0
v = 0
while i<7:
    if i<4:
        z = 4
        while z>a:
            print(" ", end="")
            z=z-1
        j = 1
        d = 5
        while j<=a:
            print(d-p, end="")
            j=j+1
            d=d-1
        g = 1
        while(g<=i):
            print(g+1,end="")
            g = g+1
    else:
        if i>=4:
            w = 4
            while w<=i:
                print(" ", end="")
                w=w+1
            o = 5
            m = 7
            while(o<=s):
                print(m-v,end="")
                o = o+1
                m = m-1
            l = 1
            while(l<=k):
                print(l+1,end="")
                l = l+1
    print()
    k = k-1  
    s = s+1
    i = i+1
    p = p-1
    a = a+1 
    v = v+1 