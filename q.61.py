i = 0
a = 5
while(i<=5):
    s = 1
    while(s<=i):
        print(" ",end="")
        s = s+1
    j = 1
    d = 1
    while(j<=a):
        print(d+i,end=" ")
        j = j+1
        d = d+1
    a = a - 1
    print()
    i = i+1
