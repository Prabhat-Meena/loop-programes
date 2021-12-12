a = "AB"
i = 1
while(i<=5):
    if i>=3:
        if i<4:
            g = 0
            while(g<1):
                print(a[g],end="")
                g = g+1
        else:
            if i<5:
                k = 2
                d = 1
                while(k<=i-1):
                    print(a[d],end="")
                    d = d-1
                    k = k+1

    if i<=1:
        print(a[0],end="")
    else:
        b = 1
        c = 1
        while(b<=2):
            print(a[c],end="")
            b = b+1
            c = c-1
    i = i+1
    print()