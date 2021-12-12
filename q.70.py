#z = "ABCD"
#n = 4
i = 1
a = 4
k = 0
while(i<=7):
    if i<7:
    #s = 1
    #while(s<=i):
    #    print("",end="")
    #    s = s+1
        j = 1
        d = 0
        while(j<=a):
            print(d+i,end="")
            j = j+1
            d = d+1
        j = 1
        while j<=k:
            print(j,end="")
            j=j+1
    else:
        print(k,end="")
    k=k+1
    print()
    a = a-2
    i = i+2