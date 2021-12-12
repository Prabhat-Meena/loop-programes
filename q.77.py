i = 1
b = 0
c = 1
while(i<=5):
    a = 1
    while(i%2==0 and a<=i):
        if a%2!=0:
            print(b,end="")
            a = a+1
        else:
            print(c,end="")
            a = a+1
    j = 1
    while(i%2!=0 and j<=i):
        if j%2==0:               
            print(b,end="")
            j = j+1
        else:
            print(c,end="")
            j = j+1
    i = i+1
    print()