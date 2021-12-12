al = "ABCD"
a = 1
i = 0
p = 5
while a<4:
    z = 3
    while z>=a:
        print(" ", end="")
        z=z-1
    b = 0
    while b<a:
        print(al[b], end="")
        b=b+1
    j = 1
    d = 4
    while(j<a):
            print(al[d-p],end="")
            j = j+1
            d = d-1
    a = a+1
    print()
    p = p-1
    i = i +1



ap2 = "ABCD"
a = 4
i = 1
p = 0
while(p<4):
    b = 1
    while(b<i):
        print(" ",end="")
        b = b+1
    j = 0
    while(j<a):
        print(ap2[j],end="")
        j = j+1
    j = 1
    d = 3
    while(j<a):
        print(ap2[d-i],end="")
        j = j+1
        d = d-1
    a = a-1
    print()
    i = i+1
    p = p+1