i = 1
while(i<=10):
    if i<10:
        b = 0
        while(b<1):
            print("*",end="")
            b = b+1
        j = 3
        while(j<=i):
            print(" ",end="")
            j = j+1
        if i>1 and i<10:
            c = 1
            while(c<=1):
                print("*",end="")
                c = c+1
    else:
        if i>9:
            a = 1
            while(a<=10):
                print("*",end="")
                a = a+1
    print()
    i = i+1

