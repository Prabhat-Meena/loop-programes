a = 5
i = 1
p = 0
while(p<=4):
    b = 1
    while(b<=i):
        print(" ",end=" ")
        b = b+1
    j = 1
    while(j<=a):
        print(j,end=" ")
        j = j+1
    j = 1
    d = 5
    while(j<a):
        print(d-i,end=" ")
        j = j+1
        d = d-1
    a = a-1
    print()
    i = i+1
    p = p+1