i = 0
a = 5
k = 4
while(i<5):
    b = 1
    while b<=i:
        print(" ", end="")
        b=b+1
    j = 1
    d = 5
    while(j<=a):
        print(d-i,end="")
        j = j+1
        d = d-1
    l = 1
    while(l<=k):
        print(l+1,end="")
        l = l+1
    print()
    k = k-1  
    a = a-1
    i = i+1  