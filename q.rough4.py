a = 2
p = 4
while(a<+4):
    if a<=1:
        print("  ",end='')
    elif a>1:
        b = 1
        while(b<=2):
            print(b,end="")
            b = b+1
    z = 2
    while(z>=a):
        print(" ",end="")
        z = z-1
    j = 1
    d = 5
    if a>1:
        while(j<=a):
            print(d-p,end="")
            j = j+1
            d = d-1
    a = a+1
    print()
    p = p-1

