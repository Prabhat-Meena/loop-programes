g = "ABC"
a = 3
while(a>=1):
    i = 0
    while(i<a):
        print(g[i],end='')
        i = i + 1
    
    if a>1:
        if a ==2:
            print(" ",end="")
        b = 1
        while(b>=0):
            print(g[b],end='')
            b = b-1
    else:
        h = 1
        while(h<=1):
            print("  ","A",end="")
            h = h+1
    print()
    a=a-1

