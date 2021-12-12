i = 1
b = 0
c = 1
while(i<=5):
    a = 1
    while(i%2==0 and i<=2 and a<=i):
        if a%2!=0:
            print(b,end="")
            a = a+1
        else:
            print(c,end="")
            a = a+1
        g = 1
    while(i%2==0 and i>=4 and g<=i):
        if(g%2==0):
            print(b,end="")
            g = g+1
        else:
            print(c,end="")
            g = g+1
    k = 1
    while(i%2!=0 and i==3 and k<=i):
        if k%2==0:
            print(c,end="")
            k = k+1
        else:
            print(b,end="")
            k = k+1
    j = 1
    while(i%2!=0 and (i<=1 or i>=5) and j<=i):
        if j%2==0:               
            print(b,end="")
            j = j+1
        else:
            print(c,end="")
            j = j+1
    i = i+1
    print()