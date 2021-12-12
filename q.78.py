i = 1
while(i<=4):
    z = 1
    while((i<=1 or i==4) and z<=1):
        print(" ",end="")
        z = z+1
    b = 1
    while((i<=1 or i==4) and b<=5):
        print("*",end="")
        b = b+1
    j = 1
    while(i>1 and i<=3 and j<=1):
        print("*",end="")
        j = j+1
    c = 1
    while(i>1 and i<=3 and c<=5):
        print(" ",end="")
        c = c+1
    d = 1
    while(i>1 and i<=3 and d<=1):
        print("*",end="")
        d = d+1
    i = i+1
    print()