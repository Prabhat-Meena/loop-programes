a = "ABCDE"
i = 4
g = 0
j = 0
while(i>0):
    if i<=2:
        w = 1
        while(w<=2):
            print(" ",end=" ")
            w = w+1
    b = 0
    while(b<=i):
        print(a[b+g],end=" ")
        b = b+1
    b = 3
    while(b>=j):
        print(a[b],end=" ")
        b = b-1
    i = i-1
    print()
    g = g+1
    j = j+1
