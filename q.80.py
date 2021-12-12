i = 1
while(i<=5):
    b = 1
    while((i%2==0 and b%2!=0)or (i%2!=0 and b%2==0) and b<=i):
        print("*",end="")
        b = b+1
    else:
        print(b,end="")
        b = b+1

    #c = 1
    #while((i%2!=0 or c%2==0) and  c<=i):
        #print(c,end="")
        #c = c+1
    i = i+1
    print()
