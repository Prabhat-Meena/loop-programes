i = 0
a = 4
k = 1
while(i<4):
    s = 1
    while(s<=i):
        print("",end="")
        s = s+1
    j = 1
    d = 1
    while(j<=a):
        print(d+i,end="")
        j = j+1
        d = d+1
    j = 1
    while j<k:
        print(j, end="")
        j=j+1
    k=k+1
    print()
    a = a-1
    i = i+1

    
    
