z = "ABCD"
i = 0
a = 4
k = 0
while(i<=7):
    if i<6:
    #s = 1
    #while(s<=i):
    #    print("",end="")
    #    s = s+1
        j = 1
        d = 0
        while(j<=a):
            print(z[d+i],end="")
            j = j+1
            d = d+1
        j = 0
        while j<k:
            print(z[j],end="")
            j=j+1
        k=k+1
    else:
        print("C",end="")
    print()
    a = a-2
    i = i+2