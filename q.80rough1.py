i = 1
while(i<=5):
    #if i%2==0:
    a = 1
    while(i%2==0 and a<=i):
            #if i%2==0 and a%2!=0:
        if a%2!=0:
            print("*",end="")
            a = a+1
        else:
            print(a,end="")
            a = a+1
    #else:
    j = 1
    while(i%2!=0 and j<=i):
            #if i%2!=0 and j%2==0:
        if j%2==0:               
            print("*",end="")
            j = j+1
        else:
            print(j,end="")
            j = j+1
    i = i+1
    print()