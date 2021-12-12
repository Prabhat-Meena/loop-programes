a = "ABCD"
b = len(a)
i = 1
d = 0
while(i<=b):
    if i%2==0:
        c = 0
        while(c<=i-1):
            print(" ",a[d],end="")
            c = c+1
        #g = 0
        #while(g<=i-1):
        #    print(a[d],end=" ")
        #    g = g+1
    else:
        c = 0
        while(c<=i-1):
            print(a[d],end=" ")
            c = c+1
    i = i+1
    d = d+1
    print()
