al = "abcde"
i = 0
a = 1
p = 4
x = 5
n = 6
while(i<5):
    j = 1
    d = 5 
    while(j<=a):
        print(d-p,end="")
        j = j+1
        d = d-1
    y = 1
    while y<=n:
        print(" ",end="")
        y=y+1
    j = 1
    d = 5
    while(j<=a):
            print(al[d-x],end="")
            j = j+1 
            d = d-1     
    a = a+1
    print()
    p = p-1
    i = i +1
    x = x-1
    n=n-1
