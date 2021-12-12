al = "ABCD"
a = 1
i = 0
p = 5
while a<=4:
    z = 4
    while z>=a:
        print(" ", end=" ")
        z=z-1
    b = 0
    while b<a:
        print(al[b], end=" ")
        b=b+1
    j = 1
    d = 4
    while(j<a):
            print(al[d-p],end=" ")
            j = j+1
            d = d-1
    a = a+1
    print()
    p = p-1
    i = i +1