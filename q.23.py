al = "ABCDE"
a = 1
i = 0
p = 5
y = 1
while a<=5:
    if y<=2:
        v = 1
        while(v<=2):
            print("  ",end=" ")
            v = v+1
        y = y+1
    else:
        if i>1 and i<3:
            print(" ",end="")
        elif i>2 and i<4:
            print("  ",end="")
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