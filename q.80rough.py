i = 1
while(i<=5):
    b = 1
    while(b<=i):
        if(i<=1):
            print(b,end="")
        elif i==2 and b%2!=0:
            print("*",end="")
        elif(i==2 and b%2==0):
            print(b,end="")
        elif(i==3 and b%2!=0):
            print(b,end="")
        elif(i==3 and b%2==0):
            print("*",end="")
        elif(i==4 and b%2!=0):
            print("*",end="")
        elif(i==4 and b%2==0):
            print(b,end="")
        elif(i==5 and b%2==0):
            print("*",end="")
        elif(i==5 and b%2!=0):
            print(b,end="")
        b = b+1
    i = i+1
    print()